import unittest
import os
from education.pipeline.orchestrator import EducationalPipeline


class TestGeneratePresentation(unittest.TestCase):

    def test_generate_presentation_returns_path(self):
        pipeline = EducationalPipeline()
        output_path = pipeline.generate_presentation("Blockchain")

        self.assertIsInstance(output_path, str)
        self.assertTrue(os.path.isfile(output_path))


if __name__ == '__main__':
    unittest.main()
