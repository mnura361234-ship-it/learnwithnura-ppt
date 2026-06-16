from pptx.util import Inches

from .base_layout import BaseLayout
from utils import add_topic_image, create_textbox


class ReversedLayout(BaseLayout):
    name = "reversed"

    def render(self, slide, title, body, context):
        theme = context["theme"]

        add_topic_image(
            slide,
            context["image_path"],
            left=Inches(0.6),
            top=Inches(1.5),
            width=Inches(3.8),
            height=Inches(3.8),
        )

        create_textbox(
            slide,
            Inches(5.0),
            Inches(0.7),
            Inches(7.0),
            Inches(0.6),
            title,
            theme,
            font_size=22,
            bold=True,
        )

        create_textbox(
            slide,
            Inches(5.0),
            Inches(1.7),
            Inches(7.0),
            Inches(3.6),
            body,
            theme,
            font_size=16,
        )
