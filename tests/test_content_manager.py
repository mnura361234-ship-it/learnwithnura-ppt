import os
import unittest

from content_manager import (
    create_content_from_template,
    list_templates,
    load_template,
    populate_placeholders,
    save_to_slides,
    validate_generated_content,
)


class TestContentManager(unittest.TestCase):
    def test_list_templates_returns_templates(self):
        templates = list_templates()
        self.assertIn('generic_template', templates)

    def test_load_template_raises_for_missing(self):
        with self.assertRaises(FileNotFoundError):
            load_template('missing_template')

    def test_populate_placeholders_replaces_known_values(self):
        text = 'Hello {{TOPIC}} and {{BRAND_NAME}}.'
        replaced = populate_placeholders(text, {'TOPIC': 'AI', 'BRAND_NAME': 'LearnWithNura'})
        self.assertEqual(replaced, 'Hello AI and LearnWithNura.')

    def test_populate_placeholders_leaves_unknown(self):
        text = 'Hello {{TOPIC}} and {{UNKNOWN}}.'
        replaced = populate_placeholders(text, {'TOPIC': 'AI'})
        self.assertEqual(replaced, 'Hello AI and {{UNKNOWN}}.')

    def test_validate_generated_content_accepts_valid_blocks(self):
        content = 'Title\nBody\n\n[comparison]\nLeft::Right\n'
        self.assertTrue(validate_generated_content(content))

    def test_validate_generated_content_rejects_empty_content(self):
        self.assertFalse(validate_generated_content('   '))

    def test_save_to_slides_writes_file(self):
        content = 'One\nTwo\n'
        save_to_slides(content)
        self.assertTrue(os.path.exists('slides.txt'))
        with open('slides.txt', 'r', encoding='utf-8') as file_handle:
            self.assertEqual(file_handle.read(), content)


if __name__ == '__main__':
    unittest.main()
