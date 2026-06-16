import argparse
import os
import sys

from backup_manager import create_backup
from content_manager import (
    create_content_from_template,
    list_templates,
    load_template,
    save_to_slides,
    validate_generated_content,
)
from config import DEFAULT_PROVIDER, DEFAULT_TEMPLATE
from developer_tools import show_project_summary
from project_manager import (
    check_required_directories,
    check_required_files,
    get_output_path,
    print_build_summary,
    resolve_topic_image,
    validate_config,
    validate_slides,
)
from providers import get_provider, list_providers
from version import PROJECT_NAME, VERSION


def parse_args():
    parser = argparse.ArgumentParser(
        description="LearnWithNura build manager",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--health", action="store_true", help="Run health checks only.")
    parser.add_argument("--validate", action="store_true", help="Validate project structure only.")
    parser.add_argument("--generate", action="store_true", help="Run generation directly.")
    parser.add_argument("--list-templates", action="store_true", help="List available slide templates.")
    parser.add_argument("--use-template", metavar="TEMPLATE", help="Load a template into slides.txt.")
    parser.add_argument("--preview-template", metavar="TEMPLATE", help="Preview a template with placeholders.")
    parser.add_argument("--create-project", metavar="TEMPLATE", help="Create a new project from a template.")
    parser.add_argument("--topic", metavar="TOPIC", help="Topic name for project creation or preview.")
    parser.add_argument("--provider", metavar="PROVIDER", help="Provider to use for content generation.")
    parser.add_argument("--list-providers", action="store_true", help="List available content providers.")
    parser.add_argument("--version", action="store_true", help="Print the current LearnWithNura version.")
    parser.add_argument("--summary", action="store_true", help="Show a project summary and health overview.")
    return parser.parse_args()


def run_health_check():
    print(f"{PROJECT_NAME} v{VERSION}")
    print("Build step: Health Check")
    from developer_tools import project_health_check

    success = project_health_check()
    print("Health Check complete.\n")
    return success


def run_validation():
    print("Build step: Asset and configuration validation")
    file_errors = check_required_files()
    dir_errors = check_required_directories()
    config_errors = validate_config()
    slide_errors = validate_slides()

    image_path, image_name = resolve_topic_image()
    image_exists = bool(image_path)
    if not image_exists:
        print("Warning: topic image missing, falling back to default image.")

    checks = [
        ("Required files present", not file_errors),
        ("Required directories present", not dir_errors),
        ("Config validation", not config_errors),
        ("Slides validation", not slide_errors),
        ("Topic image resolution", image_exists),
    ]

    print_build_summary(checks)

    if file_errors or dir_errors or config_errors or slide_errors:
        for message in file_errors + dir_errors + config_errors + slide_errors:
            print(f"ERROR: {message}")
        return False

    return True


def run_generation():
    print("Build step: Generation")
    try:
        from generate import main as generate_main
    except Exception as exc:
        print(f"ERROR: Unable to import generate.py: {exc}")
        return False

    try:
        generate_main([])
    except SystemExit as exc:
        if exc.code != 0:
            print(f"ERROR: generate.py exited with status {exc.code}")
            return False
    except Exception as exc:
        print(f"ERROR: Generation failed: {exc}")
        return False

    return True


def run_build():
    print("Build Started")
    if not run_health_check():
        print("Build failed during health check.")
        return False

    if not run_validation():
        print("Build failed during validation.")
        return False

    if not run_generation():
        print("Build failed during generation.")
        return False

    output_path = get_output_path()
    output_exists = os.path.isfile(output_path)
    print_build_summary([("Output file exists", output_exists)], output_path)

    if not output_exists:
        print(f"ERROR: Expected output file not found at {output_path}")
        return False

    print("Build Complete")
    return True


def generate_provider_content(provider_name: str, topic: str) -> bool:
    if not provider_name:
        provider_name = DEFAULT_PROVIDER

    provider = get_provider(provider_name)
    if not provider:
        print(f"ERROR: Provider '{provider_name}' not found.")
        print("Available providers:")
        for name in list_providers():
            print(f" - {name}")
        return False

    if provider_name == "manual":
        print("Using manual provider: reading slides.txt")
        try:
            _ = provider.generate(topic=topic)
        except Exception as exc:
            print(f"ERROR: Manual provider failed: {exc}")
            return False
    else:
        if not topic:
            print("ERROR: --topic is required when using provider-based generation.")
            return False
        template_name = DEFAULT_TEMPLATE
        print(f"Using provider '{provider_name}' with template '{template_name}' and topic '{topic}'")
        try:
            content = provider.generate(topic=topic, template_name=template_name)
        except FileNotFoundError as exc:
            print(f"ERROR: {exc}")
            return False
        except Exception as exc:
            print(f"ERROR: Provider generation failed: {exc}")
            return False

        backup_path = create_backup()
        if backup_path:
            print(f"Backup created: {backup_path}")
        save_to_slides(content)
        print("slides.txt updated from provider content.")

    print("Generating PowerPoint from current slides.txt...")
    if not run_generation():
        print("ERROR: Generation failed after provider content creation.")
        return False

    return True


def list_templates_command() -> bool:
    templates = list_templates()
    if not templates:
        print("No templates found.")
        return False

    print("Available templates:")
    for name in templates:
        print(f" - {name}")
    return True


def list_providers_command() -> bool:
    providers = list_providers()
    if not providers:
        print("No content providers found.")
        return False

    print("Available content providers:")
    for name in providers:
        print(f" - {name}")
    return True


def use_template_command(template_name: str) -> bool:
    try:
        content = load_template(template_name)
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}")
        return False

    backup_path = create_backup()
    if backup_path:
        print(f"Backup created: {backup_path}")

    slides_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "slides.txt")
    with open(slides_path, "w", encoding="utf-8") as slides_file:
        slides_file.write(content)

    print(f"Template '{template_name}' copied to slides.txt")
    return True


def preview_template_command(template_name: str, topic: str = None) -> bool:
    try:
        content = create_content_from_template(template_name, topic)
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}")
        return False

    print("\nTemplate preview:\n")
    print(content)
    return True


def create_project_command(template_name: str, topic: str, provider_name: str = None) -> bool:
    if not topic:
        print("ERROR: --topic is required when using --create-project.")
        return False

    if not provider_name:
        provider_name = "template"

    provider = get_provider(provider_name)
    if not provider:
        print(f"ERROR: Provider '{provider_name}' not found.")
        return False

    try:
        if provider_name == "manual":
            content = provider.generate(topic=topic)
        else:
            content = provider.generate(topic=topic, template_name=template_name)
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}")
        return False
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return False

    if not validate_generated_content(content):
        print("ERROR: Generated content did not validate against parser rules.")
        return False

    backup_path = create_backup()
    if backup_path:
        print(f"Backup created: {backup_path}")

    save_to_slides(content)

    output_path = get_output_path()
    print("Project creation summary:")
    print(f" - Template: {template_name}")
    print(f" - Topic: {topic}")
    print(f" - Provider: {provider_name}")
    print(f" - Backed up slides.txt to: {backup_path}")
    print(f" - slides.txt updated successfully.")
    print(f" - Output file will be generated at: {output_path}")
    return True


def main():
    args = parse_args()

    if args.health:
        success = run_health_check()
        sys.exit(0 if success else 1)

    if args.validate:
        success = run_validation()
        sys.exit(0 if success else 1)

    if args.list_templates:
        success = list_templates_command()
        sys.exit(0 if success else 1)

    if args.list_providers:
        success = list_providers_command()
        sys.exit(0 if success else 1)

    if args.version:
        print(f"{PROJECT_NAME} v{VERSION}")
        sys.exit(0)

    if args.summary:
        show_project_summary()
        sys.exit(0)

    if args.use_template:
        success = use_template_command(args.use_template)
        sys.exit(0 if success else 1)

    if args.preview_template:
        success = preview_template_command(args.preview_template, args.topic)
        sys.exit(0 if success else 1)

    if args.create_project:
        success = create_project_command(args.create_project, args.topic, args.provider)
        sys.exit(0 if success else 1)

    if args.provider:
        success = generate_provider_content(args.provider, args.topic)
        sys.exit(0 if success else 1)

    if args.generate:
        success = run_generation()
        sys.exit(0 if success else 1)

    success = run_build()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
