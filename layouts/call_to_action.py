from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

from .base_layout import BaseLayout
from utils import add_topic_image, create_textbox


class CallToActionLayout(BaseLayout):
    name = "call_to_action"

    def render(self, slide, title, body, context):
        theme = context["theme"]

        create_textbox(
            slide,
            Inches(1.2),
            Inches(1.8),
            Inches(10.5),
            Inches(0.8),
            "SAVE THIS FOR LATER",
            theme,
            font_size=28,
            bold=True,
            alignment=PP_ALIGN.CENTER,
        )

        create_textbox(
            slide,
            Inches(1.5),
            Inches(3.0),
            Inches(10.0),
            Inches(0.8),
            "Learn AI, Web3 & Technology visually.",
            theme,
            font_size=18,
            alignment=PP_ALIGN.CENTER,
        )

        create_textbox(
            slide,
            Inches(1.5),
            Inches(4.2),
            Inches(10.0),
            Inches(0.8),
            "Follow @LearnWithNura for more.",
            theme,
            font_size=18,
            bold=True,
            alignment=PP_ALIGN.CENTER,
            color=theme.accent_color,
        )

        add_topic_image(
            slide,
            context["image_path"],
            left=Inches(4.8),
            top=Inches(5.0),
            width=Inches(1.8),
            height=Inches(1.8),
        )
