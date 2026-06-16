from education.decomposer.concept_decomposer import ConceptDecomposer
from education.simplifier.simplification_engine import SimplificationEngine
from education.verifier.verification_engine import VerificationEngine
from education.models.domain_models import EducationalPackage


class EducationalPipeline:
    """
    Coordinates the Sprint 1 educational workflow.
    """

    def __init__(self):
        self.decomposer = ConceptDecomposer()
        self.simplifier = SimplificationEngine()
        self.verifier = VerificationEngine()

    def run(self, concept: str) -> EducationalPackage:
        definition = self.decomposer.process(concept)
        simplified = self.simplifier.process(definition)
        verification = self.verifier.process(simplified)

        return EducationalPackage(
            concept=definition,
            simplified=simplified,
            verification=verification,
        )