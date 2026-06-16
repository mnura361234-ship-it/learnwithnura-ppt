import os
from typing import Dict, Optional

from config import ASSETS_DIR

ICON_DIR = os.path.join(ASSETS_DIR, "icons")
ICON_DEFAULT = "record.png"

TOPIC_ICON_MAP: Dict[str, str] = {
    "artificial intelligence": "ai.png",
    "blockchain": "blockchain.png",
    "cryptocurrency": "crypto.png",
    "web 3": "web3.png",
    "web3": "web3.png",
    "crypto": "crypto.png",
    "ai": "ai.png",
}

LAYOUT_ICON_MAP: Dict[str, str] = {
    "standard": "record.png",
    "reversed": "record.png",
    "key_takeaway": "record.png",
    "comparison": "record.png",
    "call_to_action": "record.png",
}


def resolve_icon_path(icon_name: str, icon_pack: Optional[str] = None) -> Optional[str]:
    if not icon_name:
        return None

    candidates = []
    if icon_pack:
        candidates.append(os.path.join(ICON_DIR, icon_pack, icon_name))
    candidates.append(os.path.join(ICON_DIR, icon_name))
    candidates.append(os.path.join(ASSETS_DIR, icon_name))

    for candidate in candidates:
        if os.path.exists(candidate):
            return candidate

    return None


def get_topic_icon(topic: str, icon_pack: Optional[str] = None) -> Optional[str]:
    normalized = (topic or "").lower().strip()
    selected = TOPIC_ICON_MAP.get(normalized)

    if not selected:
        for keyword, filename in TOPIC_ICON_MAP.items():
            if keyword in normalized:
                selected = filename
                break

    if not selected:
        selected = ICON_DEFAULT

    return resolve_icon_path(selected, icon_pack)


def get_slide_icon(layout_type: str, icon_pack: Optional[str] = None) -> Optional[str]:
    icon_key = (layout_type or "").lower().strip()
    selected = LAYOUT_ICON_MAP.get(icon_key, ICON_DEFAULT)
    return resolve_icon_path(selected, icon_pack)


def add_icon(slide, icon_path: Optional[str], left, top, width, height):
    if not icon_path or not os.path.exists(icon_path):
        return None

    try:
        return slide.shapes.add_picture(icon_path, left, top, width=width, height=height)
    except Exception:
        return None
