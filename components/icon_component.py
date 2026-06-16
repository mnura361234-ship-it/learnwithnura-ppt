"""Reusable icon rendering component."""


class IconComponent:
    """Render an icon graphic onto a slide.

    TODO: Centralize icon placement, size, and theme-based assets.
    """

    def render(self, slide, icon_path, left, top, width, height):
        raise NotImplementedError("IconComponent.render must be implemented by the layout.")
