import importlib.util
import os
from typing import List, Tuple

from config import (
    ASSETS_DIR,
    CONFIG_PATH,
    IMAGES_DIR,
    OUTPUT_DIR,
    SLIDES_PATH,
    TEMPLATES_DIR,
)


def _load_config_module():
    if not os.path.isfile(CONFIG_PATH):
        raise FileNotFoundError("config.py is not available for validation.")

    spec = importlib.util.spec_from_file_location("project_config", CONFIG_PATH)
    if not spec or not spec.loader:
        raise ImportError("Unable to load config.py for validation.")

    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)
    return config


def check_required_directories() -> List[str]:
    errors: List[str] = []

    if not os.path.isdir(ASSETS_DIR):
        try:
            os.makedirs(ASSETS_DIR, exist_ok=True)
        except OSError as exc:
            errors.append(f"Unable to create assets folder: {exc}")

    if not os.path.isdir(IMAGES_DIR):
        try:
            os.makedirs(IMAGES_DIR, exist_ok=True)
        except OSError as exc:
            errors.append(f"Unable to create assets/images folder: {exc}")

    if not os.path.isdir(OUTPUT_DIR):
        try:
            os.makedirs(OUTPUT_DIR, exist_ok=True)
        except OSError as exc:
            errors.append(f"Unable to create output folder: {exc}")

    return errors


def check_required_files() -> List[str]:
    errors: List[str] = []

    if not os.path.isfile(CONFIG_PATH):
        errors.append("Missing required file: config.py")
    if not os.path.isfile(SLIDES_PATH):
        errors.append("Missing required file: slides.txt")

    return errors


def validate_config() -> List[str]:
    errors: List[str] = []
    try:
        config = _load_config_module()
    except Exception as exc:
        return [f"Config validation failed: {exc}"]

    if not getattr(config, "TOPIC", None):
        errors.append("config.py: TOPIC must be configured.")

    if not getattr(config, "OUTPUT_FILENAME_TEMPLATE", None):
        errors.append("config.py: OUTPUT_FILENAME_TEMPLATE must be configured.")

    if not getattr(config, "OUTPUT_DIR", None):
        errors.append("config.py: OUTPUT_DIR must be configured.")

    if not getattr(config, "SLIDES_PATH", None):
        errors.append("config.py: SLIDES_PATH must be configured.")

    try:
        if getattr(config, "OUTPUT_FILENAME_TEMPLATE", None) and getattr(config, "TOPIC", None):
            config.OUTPUT_FILENAME_TEMPLATE.format(topic=config.TOPIC.replace(" ", "_"))
    except Exception as exc:
        errors.append(f"config.py: OUTPUT_FILENAME_TEMPLATE formatting failed: {exc}")

    return errors


def validate_slides() -> List[str]:
    errors: List[str] = []

    if not os.path.isfile(SLIDES_PATH):
        errors.append("slides.txt is missing.")
        return errors

    try:
        with open(SLIDES_PATH, "r", encoding="utf-8") as reader:
            content = reader.read()
            if not content.strip():
                errors.append("slides.txt is empty.")
    except Exception as exc:
        errors.append(f"Unable to read slides.txt: {exc}")

    return errors


def get_output_path() -> str:
    config = _load_config_module()
    filename = config.OUTPUT_FILENAME_TEMPLATE.format(topic=config.TOPIC.replace(" ", "_"))
    return os.path.join(config.OUTPUT_DIR, filename)


def list_templates() -> List[str]:
    if not os.path.isdir(TEMPLATES_DIR):
        return []

    names = []
    for entry in sorted(os.listdir(TEMPLATES_DIR)):
        if entry.endswith(".txt"):
            names.append(os.path.splitext(entry)[0])
    return names


def get_template_path(template_name: str) -> str:
    return os.path.join(TEMPLATES_DIR, f"{template_name}.txt")


def load_template(template_name: str) -> str:
    template_path = get_template_path(template_name)
    if not os.path.isfile(template_path):
        raise FileNotFoundError(f"Template '{template_name}' not found.")

    with open(template_path, "r", encoding="utf-8") as template_file:
        return template_file.read()


def print_build_summary(checks: List[Tuple[str, bool]], output_path: str = None) -> None:
    print("\nBuild Summary")
    print("-------------")
    for label, passed in checks:
        status = "OK" if passed else "FAILED"
        print(f"{label:28} {status}")

    if output_path:
        print(f"Output file: {output_path}")

    print("-------------")


def resolve_topic_image():
    try:
        config = _load_config_module()
    except Exception:
        return None, None

    from image_manager import select_topic_image

    image_path, image_name = select_topic_image(config.TOPIC)
    return image_path, image_name
