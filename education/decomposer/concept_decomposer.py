from education.models.domain_models import ConceptDefinition


class ConceptDecomposer:
    """
    Converts a raw concept string into a structured ConceptDefinition.
    """

    def process(self, raw_concept: str) -> ConceptDefinition:
        return ConceptDefinition(
            concept=raw_concept,
            description=f"{raw_concept} is an important concept in modern technology.",
            prerequisites=[],
            scope="General",
            status="atomic",
            analogy_categories=["general"]
        )