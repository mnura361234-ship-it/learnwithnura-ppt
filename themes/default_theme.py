from pptx.dml.color import RGBColor

from .theme import Theme

DEFAULT_THEME = Theme(
    primary_color=RGBColor(20, 20, 20),
    secondary_color=RGBColor(110, 110, 110),
    accent_color=RGBColor(46, 109, 246),
    background_color=RGBColor(248, 249, 251),
    font_name="Calibri",
    icon_pack="default",
    background_image=None,
    decorative_shapes=[
        {"shape_type": 1, "left": 0.5, "top": 0.5, "width": 1.0, "height": 0.1, "color": RGBColor(241, 246, 255)},
    ],
)
