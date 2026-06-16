import unittest

from layouts import registry
from layouts.base_layout import BaseLayout


class TestRegistry(unittest.TestCase):
    def test_registered_layouts_are_found(self):
        names = registry.registered_layout_names()
        self.assertIn('standard', names)
        self.assertIn('timeline', names)

    def test_get_layout_class_returns_base_layout_subclass(self):
        layout_cls = registry.get_layout_class('standard')
        self.assertIsNotNone(layout_cls)
        self.assertTrue(issubclass(layout_cls, BaseLayout))

    def test_unknown_layout_returns_none(self):
        self.assertIsNone(registry.get_layout_class('not_a_layout'))


if __name__ == '__main__':
    unittest.main()
