from pptx.util import Inches

from .base_layout import BaseLayout
from utils import add_topic_image, create_textbox


class KeyTakeawayLayout(BaseLayout):
    name = "key_takeaway"

    def render(self, slide, title, body, context):
        theme = context["theme"]

        create_textbox(
            slide,
            Inches(0.8),
            Inches(0.7),
            Inches(4.5),
            Inches(0.5),
            "KEY TAKEAWAY",
            theme,
            font_size=12,
            bold=True,
            color=theme.accent_color,
        )

        create_textbox(
            slide,
            Inches(0.8),
            Inches(1.3),
            Inches(7.2),
            Inches(0.8),
            title,
            theme,
            font_size=24,
            bold=True,
        )

        create_textbox(
            slide,
            Inches(0.8),
            Inches(2.4),
            Inches(7.0),
            Inches(2.6),
            body,
            theme,
            font_size=18,
        )

        add_topic_image(
            slide,
            context["image_path"],
            left=Inches(8.9),
            top=Inches(2.0),
            width=Inches(3.2),
            height=Inches(3.2),
        )
