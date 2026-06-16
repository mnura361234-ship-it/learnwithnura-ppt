"""Reusable title rendering component."""

from utils import create_textbox


class TitleComponent:
    """Render a slide title element.

    TODO: Centralize title styling, placement, and accessibility features.
    """

    def render(
        self,
        slide,
        text,
        theme,
        left,
        top,
        width,
        height,
        font_size=22,
        bold=True,
    ):
        create_textbox(
            slide,
            left,
            top,
            width,
            height,
            text,
            theme,
            font_size=font_size,
            bold=bold,
        )
