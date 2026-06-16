"""Reusable footer rendering component."""


class FooterComponent:
    """Render slide footer content consistently.

    TODO: Encapsulate pagination, branding, and footer layout.
    """

    def render(self, slide, slide_number, theme, left, top, width, height):
        raise NotImplementedError("FooterComponent.render must be implemented by the layout.")
