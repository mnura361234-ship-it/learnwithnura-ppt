"""Developer utilities for LearnWithNura Presentation Engine."""

import os
import pkgutil
import unittest

from config import (
    DEFAULT_PROVIDER,
    ASSETS_DIR,
    BACKUP_DIR,
    COMPONENTS_DIR,
    LAYOUTS_DIR,
    OUTPUT_DIR,
    PROVIDERS_DIR,
    PROMPTS_DIR,
    TEMPLATES_DIR,
)

from layouts import registry
from providers import list_providers
from content_manager import list_templates
from version import PROJECT_NAME, VERSION


def status_label(label: str, passed: bool) -> str:
    return f"{label:30} {'PASS' if passed else 'ERROR'}"


def warn_label(label: str, warning: bool) -> str:
    return f"{label:30} {'WARNING' if warning else 'PASS'}"


def print_registered_layouts():
    """Print all layouts currently registered by the layout registry."""
    print('Registered layouts:')
    for name in registry.registered_layout_names():
        print(f' - {name}')


def print_registered_providers():
    """Print all providers currently discovered by the provider registry."""
    print('Registered providers:')
    for name in list_providers():
        print(f' - {name}')


def print_available_templates():
    """Print all slide templates available in the templates folder."""
    print('Available templates:')
    for name in list_templates():
        print(f' - {name}')


def can_write_output() -> bool:
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        test_file = os.path.join(OUTPUT_DIR, '.write_test')
        with open(test_file, 'w', encoding='utf-8') as handle:
            handle.write('ok')
        os.remove(test_file)
        return True
    except Exception:
        return False


def _verify_directory(path: str) -> bool:
    return os.path.isdir(path)


def _verify_file(path: str) -> bool:
    return os.path.isfile(path)


def project_health_check():
    """Run a detailed health check for the LearnWithNura project."""
    print('LearnWithNura Health Check')
    print('===========================')

    checks = []
    checks.append((_verify_directory(ASSETS_DIR), 'assets/ directory present'))
    checks.append((_verify_directory(TEMPLATES_DIR), 'templates/ directory present'))
    checks.append((_verify_directory(PROMPTS_DIR), 'prompts/ directory present'))
    checks.append((_verify_directory(BACKUP_DIR), 'backups/ directory present'))
    checks.append((_verify_directory(OUTPUT_DIR), 'output/ directory present'))
    checks.append((_verify_directory(LAYOUTS_DIR), 'layouts/ directory present'))
    checks.append((_verify_directory(COMPONENTS_DIR), 'components/ directory present'))
    checks.append((_verify_directory(PROVIDERS_DIR), 'providers/ directory present'))

    checks.append((_verify_file(os.path.join(os.path.dirname(__file__), 'slides.txt')), 'slides.txt present'))
    checks.append((_verify_file(os.path.join(os.path.dirname(__file__), 'config.py')), 'config.py present'))
    checks.append((_verify_file(os.path.join(os.path.dirname(__file__), 'generate.py')), 'generate.py present'))
    checks.append((_verify_file(os.path.join(os.path.dirname(__file__), 'build.py')), 'build.py present'))
    checks.append((_verify_file(os.path.join(os.path.dirname(__file__), 'parser.py')), 'parser.py present'))
    checks.append((_verify_file(os.path.join(os.path.dirname(__file__), 'topics.json')), 'topics.json present'))

    # runtime checks
    template_count = len(list_templates())
    checks.append((template_count > 0, 'templates discoverable'))
    checks.append((_verify_directory(ASSETS_DIR), 'assets folder exists'))
    checks.append((can_write_output(), 'output directory writable'))
    checks.append((len(list_providers()) > 0, 'provider registry loads'))
    checks.append((len(registry.registered_layout_names()) > 0, 'layout registry loads'))

    error_count = 0
    for passed, message in checks:
        if passed:
            print(status_label(message, True))
        else:
            print(status_label(message, False))
            error_count += 1

    if error_count == 0:
        print('\nHealth Check Result: PASS')
        return True

    print('\nHealth Check Result: ERROR')
    return False


def show_project_summary():
    """Print a project summary including version, providers, layouts, templates, component count, and health."""
    print('Project Summary')
    print('===============')
    print(f'Project        : {PROJECT_NAME}')
    print(f'Version        : {VERSION}')
    print(f'Active Provider: {DEFAULT_PROVIDER}')
    print(f'Assets Dir     : {ASSETS_DIR}')
    print(f'Output Dir     : {OUTPUT_DIR}')
    print(f'Templates Dir  : {TEMPLATES_DIR}')
    print(f'Prompts Dir    : {PROMPTS_DIR}')
    print(f'Providers Dir  : {PROVIDERS_DIR}')
    print(f'Layouts Dir    : {LAYOUTS_DIR}')
    print(f'Components Dir : {COMPONENTS_DIR}')
    print(f'Backup Dir     : {BACKUP_DIR}')

    print('\nAvailable providers:')
    print_registered_providers()
    print('\nAvailable layouts:')
    print_registered_layouts()
    print('\nAvailable templates:')
    print_available_templates()

    component_count = sum(1 for _ in pkgutil.iter_modules([COMPONENTS_DIR]))
    print(f'Component count: {component_count}')

    test_loader = unittest.TestLoader()
    tests = test_loader.discover('tests')
    print(f'Test modules    : {len(tests._tests) if hasattr(tests, "_tests") else "unknown"}')

    print('\nProject health:')
    project_health_check()


if __name__ == '__main__':
    show_project_summary()
