from pptx.util import Inches

from .base_layout import BaseLayout
from utils import create_textbox, split_comparison


class ComparisonLayout(BaseLayout):
    name = "comparison"

    def render(self, slide, title, body, context):
        theme = context["theme"]
        left_text, right_text = split_comparison(body)

        create_textbox(
            slide,
            Inches(0.8),
            Inches(0.6),
            Inches(8.0),
            Inches(0.6),
            title,
            theme,
            font_size=22,
            bold=True,
        )

        create_textbox(
            slide,
            Inches(0.8),
            Inches(1.5),
            Inches(5.2),
            Inches(0.4),
            "Option A",
            theme,
            font_size=14,
            bold=True,
            color=theme.accent_color,
        )

        create_textbox(
            slide,
            Inches(7.0),
            Inches(1.5),
            Inches(5.2),
            Inches(0.4),
            "Option B",
            theme,
            font_size=14,
            bold=True,
            color=theme.accent_color,
        )

        create_textbox(
            slide,
            Inches(0.8),
            Inches(2.0),
            Inches(5.2),
            Inches(3.2),
            left_text,
            theme,
            font_size=15,
        )

        create_textbox(
            slide,
            Inches(7.0),
            Inches(2.0),
            Inches(5.2),
            Inches(3.2),
            right_text,
            theme,
            font_size=15,
        )
