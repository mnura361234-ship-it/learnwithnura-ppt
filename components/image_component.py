"""Reusable image placement component."""

from utils import add_topic_image


class ImageComponent:
    """Render an image element on a slide.

    TODO: Standardize image placement, scaling, and fallback handling.
    """

    def render(self, slide, image_path, left, top, width, height):
        add_topic_image(
            slide,
            image_path,
            left=left,
            top=top,
            width=width,
            height=height,
        )
