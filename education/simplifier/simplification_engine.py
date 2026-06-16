from education.models.domain_models import (
    ConceptDefinition,
    SimplifiedConcept,
)


class SimplificationEngine:
    """
    Converts a technical concept into beginner-friendly language.
    """

    def process(self, concept: ConceptDefinition) -> SimplifiedConcept:
        plain = (
            f"{concept.concept} is a simple idea that can be understood "
            f"without needing advanced technical knowledge."
        )

        return SimplifiedConcept(
            original=concept,
            plain_language=plain,
            glossary={
                concept.concept.lower(): concept.description
            },
            complexity_score=0.20,
            metadata={
                "version": "sprint1"
            }
        )