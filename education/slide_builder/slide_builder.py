from typing import Dict, List

from education.models.domain_models import EducationalPackage


class SlideBuilder:
    """
    Converts an EducationalPackage into structured slide content.

    This layer bridges the Education OS and the Presentation Engine by returning
    lightweight slide dictionaries that can later be rendered into a PowerPoint.
    """

    def build(self, package: EducationalPackage) -> List[Dict[str, str]]:
        """
        Build a simple educational slide deck from an EducationalPackage.

        Returns a list of slide dictionaries with `layout`, `title`, and `body`.
        """
        concept = package.concept
        simplified = package.simplified
        verification = package.verification

        return [
            {
                "layout": None,
                "title": f"{concept.concept}",
                "body": concept.scope or concept.description,
            },
            {
                "layout": "standard",
                "title": "What is the concept?",
                "body": concept.description or f"An introduction to {concept.concept}.",
            },
            {
                "layout": "standard",
                "title": "Simple Explanation",
                "body": simplified.plain_language or "A beginner-friendly explanation is not available yet.",
            },
            {
                "layout": "standard",
                "title": "Key Points / Breakdown",
                "body": self._build_key_points(concept, simplified),
            },
            {
                "layout": "call_to_action",
                "title": "Conclusion",
                "body": self._build_conclusion(verification),
            },
        ]

    def _build_key_points(self, concept, simplified) -> str:
        points = []

        if concept.prerequisites:
            points.append("Prerequisites: " + ", ".join(concept.prerequisites))

        if simplified.glossary:
            glossary_terms = ", ".join(simplified.glossary.keys())
            points.append("Glossary terms: " + glossary_terms)

        if concept.analogy_categories:
            points.append("Analogy categories: " + ", ".join(concept.analogy_categories))

        if not points:
            points.append("No additional breakdown available yet.")

        return "\n".join(points)

    def _build_conclusion(self, verification) -> str:
        status = "passed" if verification.passed else "requires review"
        lines = [
            f"Verification status: {status}.",
            f"Accuracy score: {verification.accuracy_score:.2f}",
            f"Simplicity score: {verification.simplicity_score:.2f}",
        ]

        if verification.recommendations:
            lines.append("Recommendations: " + "; ".join(verification.recommendations))

        return "\n".join(lines)
