import importlib.util
import os
import pkgutil
from typing import Dict, Type

from .base_provider import BaseContentProvider

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))

_PROVIDERS: Dict[str, Type[BaseContentProvider]] = {}


def register_provider(provider_cls: Type[BaseContentProvider]) -> None:
    if not isinstance(provider_cls, type):
        return
    if not issubclass(provider_cls, BaseContentProvider):
        return

    name = getattr(provider_cls, "name", None)
    if not name or not isinstance(name, str):
        return

    _PROVIDERS[name] = provider_cls


def get_provider(name: str):
    provider_cls = _PROVIDERS.get(name)
    return provider_cls() if provider_cls else None


def list_providers():
    return sorted(_PROVIDERS)


def _discover_providers():
    for finder, module_name, is_pkg in pkgutil.iter_modules([PACKAGE_DIR]):
        if module_name == "__init__":
            continue

        module_path = os.path.join(PACKAGE_DIR, f"{module_name}.py")
        if not os.path.isfile(module_path):
            continue

        try:
            spec = importlib.util.spec_from_file_location(f"providers.{module_name}", module_path)
            if not spec or not spec.loader:
                continue

            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)
                if (
                    isinstance(attribute, type)
                    and issubclass(attribute, BaseContentProvider)
                    and attribute is not BaseContentProvider
                ):
                    register_provider(attribute)
        except Exception:
            continue


_discover_providers()
