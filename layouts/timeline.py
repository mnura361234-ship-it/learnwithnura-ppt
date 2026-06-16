from pptx.util import Inches

from .base_layout import BaseLayout
from utils import add_topic_image, create_textbox, parse_timeline, draw_timeline


class TimelineLayout(BaseLayout):
    name = "timeline"

    def render(self, slide, title, body, context):
        theme = context["theme"]

        create_textbox(
            slide,
            Inches(0.8),
            Inches(0.6),
            Inches(11.0),
            Inches(0.7),
            title,
            theme,
            font_size=26,
            bold=True,
        )

        entries = parse_timeline(body)
        if entries:
            draw_timeline(slide, entries, theme, context.get('slide_width'))
        else:
            create_textbox(
                slide,
                Inches(0.8),
                Inches(2.5),
                Inches(10.5),
                Inches(3.5),
                body,
                theme,
                font_size=16,
            )

        add_topic_image(
            slide,
            context["image_path"],
            left=Inches(8.0),
            top=Inches(4.5),
            width=Inches(3.5),
            height=Inches(3.5),
        )
