"""Reusable body text rendering component."""

from utils import create_textbox


class BodyComponent:
    """Render a body text block on a slide.

    TODO: Encapsulate paragraph formatting, growable text boxes,
    and list rendering behavior.
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
        font_size=16,
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
        )
