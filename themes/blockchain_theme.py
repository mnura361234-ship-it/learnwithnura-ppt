from pptx.dml.color import RGBColor

from .theme import Theme

BLOCKCHAIN_THEME = Theme(
    primary_color=RGBColor(20, 20, 20),
    secondary_color=RGBColor(100, 115, 135),
    accent_color=RGBColor(46, 109, 246),
    background_color=RGBColor(241, 246, 255),
    font_name="Calibri",
    icon_pack="default",
    background_image=None,
)
