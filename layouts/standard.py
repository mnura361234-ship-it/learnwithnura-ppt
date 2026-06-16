from pptx.util import Inches

from .base_layout import BaseLayout
from components.body_component import BodyComponent
from components.image_component import ImageComponent
from components.title_component import TitleComponent


class StandardLayout(BaseLayout):
    name = "standard"

    def render(self, slide, title, body, context):
        theme = context["theme"]

        TitleComponent().render(
            slide,
            title,
            theme,
            left=Inches(0.7),
            top=Inches(0.6),
            width=Inches(6.2),
            height=Inches(0.6),
            font_size=22,
            bold=True,
        )

        BodyComponent().render(
            slide,
            body,
            theme,
            left=Inches(0.7),
            top=Inches(1.6),
            width=Inches(6.2),
            height=Inches(3.8),
            font_size=16,
        )

        ImageComponent().render(
            slide,
            context["image_path"],
            left=Inches(8.7),
            top=Inches(1.35),
            width=Inches(3.8),
            height=Inches(3.8),
        )
