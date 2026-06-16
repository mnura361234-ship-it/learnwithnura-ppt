from pptx.dml.color import RGBColor

from .theme import Theme

AI_THEME = Theme(
    primary_color=RGBColor(20, 20, 20),
    secondary_color=RGBColor(100, 100, 120),
    accent_color=RGBColor(109, 46, 246),
    background_color=RGBColor(245, 242, 255),
    font_name="Calibri",
    icon_pack="default",
    background_image=None,
)
