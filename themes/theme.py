from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from pptx.dml.color import RGBColor


@dataclass(frozen=True)
class Theme:
    primary_color: RGBColor
    secondary_color: RGBColor
    accent_color: RGBColor
    background_color: RGBColor
    font_name: str
    icon_pack: Optional[str] = None
    background_image: Optional[str] = None
    decorative_shapes: Optional[List[Dict[str, Any]]] = None
