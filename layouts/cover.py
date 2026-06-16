from pptx.util import Inches

from .base_layout import BaseLayout
from utils import add_topic_image, create_textbox


class CoverLayout(BaseLayout):
    name = "cover"

    def render(self, slide, title, body, context):
        theme = context["theme"]

        create_textbox(
            slide,
            left=Inches(0.8),
            top=Inches(2.0),
            width=Inches(6.0),
            height=Inches(0.8),
            text=title,
            theme=theme,
            font_size=30,
            bold=True,
        )

        create_textbox(
            slide,
            left=Inches(0.8),
            top=Inches(3.0),
            width=Inches(5.5),
            height=Inches(0.5),
            text=body or "LearnWithNura • AI | Web3 | Blockchain | Technology",
            theme=theme,
            font_size=14,
            color=theme.secondary_color,
        )

        add_topic_image(
            slide,
            context["image_path"],
            left=Inches(8.3),
            top=Inches(1.5),
            width=Inches(4.2),
            height=Inches(4.2),
        )
