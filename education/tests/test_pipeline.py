import unittest

from education.pipeline.orchestrator import EducationalPipeline


class TestEducationalPipeline(unittest.TestCase):

    def test_pipeline_creation(self):
        pipeline = EducationalPipeline()
        self.assertIsInstance(pipeline, EducationalPipeline)


if __name__ == "__main__":
    unittest.main()