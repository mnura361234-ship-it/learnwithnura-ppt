from pptx.dml.color import RGBColor

from .theme import Theme

CRYPTO_THEME = Theme(
    primary_color=RGBColor(20, 20, 20),
    secondary_color=RGBColor(90, 110, 110),
    accent_color=RGBColor(37, 169, 102),
    background_color=RGBColor(241, 255, 246),
    font_name="Calibri",
    icon_pack="default",
    background_image=None,
)
