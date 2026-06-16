from abc import ABC, abstractmethod

from icon_manager import add_icon
from pptx.util import Inches
from utils import add_background, add_footer


class BaseLayout(ABC):
    name = "base"

    def create_slide(self, prs, context):
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        add_background(slide, context["theme"], context["slide_height"])
        return slide

    @abstractmethod
    def render(self, slide, title, body, context):
        raise NotImplementedError

    def build(self, prs, title, body, context):
        slide = self.create_slide(prs, context)
        self.render(slide, title, body, context)

        icon_path = context.get("slide_icon")
        if icon_path:
            add_icon(slide, icon_path, Inches(11.0), Inches(0.4), Inches(0.6), Inches(0.6))

        add_footer(slide, context["slide_number"], context["theme"])
        return slide
