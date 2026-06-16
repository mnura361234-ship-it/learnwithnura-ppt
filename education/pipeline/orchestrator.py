from education.decomposer.concept_decomposer import ConceptDecomposer
from education.simplifier.simplification_engine import SimplificationEngine
from education.verifier.verification_engine import VerificationEngine
from education.models.domain_models import EducationalPackage
from education.slide_builder.slide_builder import SlideBuilder
from education.presentation_adapter.presentation_adapter import PresentationAdapter
import build as build_module


class EducationalPipeline:
    """
    Coordinates the Sprint 1 educational workflow.
    """

    def __init__(self):
        self.decomposer = ConceptDecomposer()
        self.simplifier = SimplificationEngine()
        self.verifier = VerificationEngine()
        self.slide_builder = SlideBuilder()
        self.presentation_adapter = PresentationAdapter()

    def run(self, concept: str) -> EducationalPackage:
        definition = self.decomposer.process(concept)
        simplified = self.simplifier.process(definition)
        verification = self.verifier.process(simplified)

        return EducationalPackage(
            concept=definition,
            simplified=simplified,
            verification=verification,
        )
    def generate_slide_content(self, concept: str):
        """
        Run the educational pipeline and convert the resulting package into slide content.

        This method preserves the existing pipeline behavior while adding a
        lightweight integration point for the Presentation Engine.
        """
        package = self.run(concept)
        return self.slide_builder.build(package)

    def generate_presentation(self, concept: str):
        """
        High-level convenience method that runs the educational pipeline,
        converts the result into slides, prepares them via the PresentationAdapter,
        and invokes the existing build workflow to produce a PowerPoint.

        Returns the path to the generated PowerPoint file on success.
        """
        # 1) Run the pipeline
        package = self.run(concept)

        # 2) Build slides (list of dicts)
        slides = self.slide_builder.build(package)

        # 3) Convert to slides.txt format and persist
        slides_content = self.presentation_adapter.prepare(slides)

        # 4) Invoke the build pipeline to generate the PPTX
        # Use the existing `build.run_build()` to preserve orchestration
        success = build_module.run_build()
        if not success:
            raise RuntimeError("Build system failed to generate presentation.")

        # 5) Return the expected output path from project_manager.get_output_path
        from project_manager import get_output_path

        return get_output_path()
