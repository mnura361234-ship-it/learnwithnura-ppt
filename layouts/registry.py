import importlib.util
import os
import pkgutil
from typing import Dict, List, Optional, Type

from .base_layout import BaseLayout

PACKAGE_DIR = os.path.dirname(__file__)

_LAYOUT_REGISTRY: Dict[str, Type[BaseLayout]] = {}


def register_layout(layout_cls: Type[BaseLayout]) -> None:
    """Register a layout class by its declared name."""
    if not isinstance(layout_cls, type):
        return
    if not issubclass(layout_cls, BaseLayout):
        return

    name = getattr(layout_cls, "name", None)
    if not name or not isinstance(name, str):
        return

    _LAYOUT_REGISTRY[name] = layout_cls


def get_layout_class(name: str) -> Optional[Type[BaseLayout]]:
    return _LAYOUT_REGISTRY.get(name)


def get_all_layouts() -> Dict[str, Type[BaseLayout]]:
    return dict(_LAYOUT_REGISTRY)


def registered_layout_names() -> List[str]:
    return sorted(_LAYOUT_REGISTRY)


def _discover_layouts() -> None:
    """Discover all valid layout modules in the layouts package."""
    for finder, module_name, is_pkg in pkgutil.iter_modules([PACKAGE_DIR]):
        if module_name == "__init__":
            continue

        module_path = os.path.join(PACKAGE_DIR, f"{module_name}.py")
        if not os.path.exists(module_path):
            continue

        try:
            spec = importlib.util.spec_from_file_location(f"layouts.{module_name}", module_path)
            if not spec or not spec.loader:
                continue

            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)
                if (
                    isinstance(attribute, type)
                    and issubclass(attribute, BaseLayout)
                    and attribute is not BaseLayout
                ):
                    register_layout(attribute)
        except Exception:
            continue


_discover_layouts()
