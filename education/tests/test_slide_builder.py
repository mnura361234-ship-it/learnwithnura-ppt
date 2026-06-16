import unittest

from education.pipeline.orchestrator import EducationalPipeline
from education.slide_builder.slide_builder import SlideBuilder


class TestSlideBuilder(unittest.TestCase):

    def test_slide_builder_generates_valid_slides(self):
        pipeline = EducationalPipeline()
        package = pipeline.run("Blockchain")

        slides = SlideBuilder().build(package)

        self.assertTrue(slides)
        self.assertGreaterEqual(len(slides), 5)

        for slide in slides:
            self.assertIsInstance(slide, dict)
            self.assertIn("layout", slide)
            self.assertIn("title", slide)
            self.assertIn("body", slide)
            self.assertTrue(slide["layout"])
            self.assertTrue(slide["title"])
            self.assertTrue(slide["body"])

    def test_pipeline_generates_slide_content(self):
        pipeline = EducationalPipeline()
        slides = pipeline.generate_slide_content("Blockchain")

        self.assertIsInstance(slides, list)
        self.assertGreaterEqual(len(slides), 5)
        self.assertTrue(all(isinstance(slide, dict) for slide in slides))


if __name__ == "__main__":
    unittest.main()
