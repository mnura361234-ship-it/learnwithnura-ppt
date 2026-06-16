import os
import tempfile
import unittest

import parser


class TestParser(unittest.TestCase):
    def setUp(self):
        self.original_path = parser.SLIDES_PATH
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_file = os.path.join(self.temp_dir.name, 'slides.txt')
        parser.SLIDES_PATH = self.test_file

    def tearDown(self):
        parser.SLIDES_PATH = self.original_path
        self.temp_dir.cleanup()

    def write_slides(self, content):
        with open(self.test_file, 'w', encoding='utf-8') as handle:
            handle.write(content)

    def test_legacy_parsing(self):
        self.write_slides('Title 1\nBody 1\n\nTitle 2\nBody 2\n')
        slides = parser.load_slides()
        self.assertEqual(len(slides), 2)
        self.assertEqual(slides[0].title, 'Title 1')
        self.assertEqual(slides[0].body, 'Body 1')

    def test_structured_block_parsing(self):
        content = '[standard]\nTitle\nBody line 1\nBody line 2\n'
        self.write_slides(content)
        slides = parser.load_slides()
        self.assertEqual(len(slides), 1)
        self.assertEqual(slides[0].layout, 'standard')
        self.assertEqual(slides[0].title, 'Title')
        self.assertEqual(slides[0].body, 'Body line 1\nBody line 2')

    def test_layout_declaration_parsing(self):
        content = '[timeline]\nTimeline title\nTimeline item\n'
        self.write_slides(content)
        slides = parser.load_slides()
        self.assertEqual(slides[0].layout, 'timeline')

    def test_multiline_body_preservation(self):
        content = 'Title\nLine 1\nLine 2\n'
        self.write_slides(content)
        slides = parser.load_slides()
        self.assertEqual(len(slides), 1)
        self.assertEqual(slides[0].body, 'Line 1\nLine 2')

    def test_odd_line_legacy_block_parsing(self):
        content = 'Title\nLine 1\nLine 2\n'
        self.write_slides(content)
        slides = parser.load_slides()
        self.assertEqual(len(slides), 1)
        self.assertEqual(slides[0].title, 'Title')
        self.assertEqual(slides[0].body, 'Line 1\nLine 2')

    def test_malformed_block_recovery(self):
        content = '[standard]\n\n\nTitle only\n\n'
        self.write_slides(content)
        slides = parser.load_slides()
        self.assertEqual(len(slides), 1)
        self.assertEqual(slides[0].title, 'Title only')
        self.assertEqual(slides[0].body, '')


if __name__ == '__main__':
    unittest.main()
