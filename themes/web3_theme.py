from pptx.dml.color import RGBColor

from .theme import Theme

WEB3_THEME = Theme(
    primary_color=RGBColor(20, 20, 20),
    secondary_color=RGBColor(100, 105, 135),
    accent_color=RGBColor(255, 102, 0),
    background_color=RGBColor(255, 244, 235),
    font_name="Calibri",
    icon_pack="default",
    background_image=None,
)
