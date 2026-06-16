from education.models.domain_models import (
    SimplifiedConcept,
    VerificationReport,
)


class VerificationEngine:
    """
    Performs basic quality checks on simplified content.
    """

    def process(self, concept: SimplifiedConcept) -> VerificationReport:
        issues = []
        recommendations = []

        if len(concept.plain_language) < 20:
            issues.append("Explanation is too short.")
            recommendations.append(
                "Provide a more detailed beginner-friendly explanation."
            )

        passed = len(issues) == 0

        return VerificationReport(
            accuracy_score=1.0,
            simplicity_score=0.95,
            passed=passed,
            issues=issues,
            recommendations=recommendations,
        )