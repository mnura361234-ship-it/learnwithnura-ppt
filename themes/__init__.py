"""Theme package for LearnWithNura PPT Generator."""
from .theme import Theme
from .default_theme import DEFAULT_THEME
from .blockchain_theme import BLOCKCHAIN_THEME
from .ai_theme import AI_THEME
from .crypto_theme import CRYPTO_THEME
from .web3_theme import WEB3_THEME

THEME_MAP = {
    "blockchain": BLOCKCHAIN_THEME,
    "ai": AI_THEME,
    "crypto": CRYPTO_THEME,
    "web3": WEB3_THEME,
}


def select_theme(topic: str) -> Theme:
    normalized = (topic or "").lower().strip()
    for keyword, theme in THEME_MAP.items():
        if normalized == keyword or keyword in normalized.split():
            return theme
    return DEFAULT_THEME

__all__ = [
    "Theme",
    "DEFAULT_THEME",
    "BLOCKCHAIN_THEME",
    "AI_THEME",
    "CRYPTO_THEME",
    "WEB3_THEME",
    "select_theme",
]
