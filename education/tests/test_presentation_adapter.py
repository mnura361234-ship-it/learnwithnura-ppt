import unittest
from education.slide_builder.slide_builder import SlideBuilder
from education.presentation_adapter.presentation_adapter import PresentationAdapter


class TestPresentationAdapter(unittest.TestCase):

    def test_adapter_prepares_valid_slides_content(self):
        # Create a minimal package via mocking basic objects
        class Simple:
            def __init__(self, concept):
                self.concept = concept
                self.description = "Desc"
                self.prerequisites = []
                self.scope = "General"
                self.analogy_categories = []

        class SimpleSimplified:
            def __init__(self):
                self.plain_language = "Simple explanation"
                self.glossary = {}

        class SimpleVerification:
            def __init__(self):
                self.passed = True
                self.accuracy_score = 1.0
                self.simplicity_score = 1.0
                self.recommendations = []

        from education.models.domain_models import EducationalPackage

        concept = Simple("Test")
        simplified = SimpleSimplified()
        verification = SimpleVerification()

        package = EducationalPackage(concept=concept, simplified=simplified, verification=verification)

        slides = SlideBuilder().build(package)
        adapter = PresentationAdapter()
        content = adapter.prepare(slides)

        self.assertIsInstance(content, str)
        self.assertIn("Test", content)
        self.assertIn("Simple explanation", content)


if __name__ == '__main__':
    unittest.main()
