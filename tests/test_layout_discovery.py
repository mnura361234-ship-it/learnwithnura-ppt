import unittest

from layouts import registry
from layouts.base_layout import BaseLayout


class TestLayoutDiscovery(unittest.TestCase):
    def test_discovered_layouts_subclass_base_layout(self):
        for name, layout_cls in registry.get_all_layouts().items():
            with self.subTest(name=name):
                self.assertTrue(issubclass(layout_cls, BaseLayout))

    def test_layout_names_are_unique(self):
        names = registry.registered_layout_names()
        self.assertEqual(len(names), len(set(names)))

    def test_layout_classes_have_name_attribute(self):
        for layout_cls in registry.get_all_layouts().values():
            self.assertTrue(hasattr(layout_cls, 'name'))
            self.assertIsInstance(getattr(layout_cls, 'name'), str)


if __name__ == '__main__':
    unittest.main()
