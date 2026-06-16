import unittest

from components.body_component import BodyComponent
from components.image_component import ImageComponent
from components.title_component import TitleComponent
from utils import draw_timeline


class TestComponents(unittest.TestCase):
    def test_title_component_instantiation(self):
        component = TitleComponent()
        self.assertTrue(hasattr(component, 'render'))

    def test_body_component_instantiation(self):
        component = BodyComponent()
        self.assertTrue(hasattr(component, 'render'))

    def test_image_component_instantiation(self):
        component = ImageComponent()
        self.assertTrue(hasattr(component, 'render'))

    def test_draw_timeline_wrapper_accepts_empty_entries(self):
        draw_timeline(None, [], None, slide_width=1)

    def test_draw_timeline_wrapper_accepts_none_entries(self):
        draw_timeline(None, None, None, slide_width=1)


if __name__ == '__main__':
    unittest.main()
