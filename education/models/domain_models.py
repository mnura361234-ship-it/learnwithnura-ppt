from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class ConceptDefinition:
    """
    Normalized representation of a concept after decomposition.
    """
    concept: str
    description: str
    prerequisites: List[str] = field(default_factory=list)
    scope: str = ""
    status: str = "atomic"  # atomic | compound
    analogy_categories: List[str] = field(default_factory=list)


@dataclass
class SimplifiedConcept:
    """
    Beginner-friendly version of a concept.
    """
    original: ConceptDefinition
    plain_language: str
    glossary: Dict[str, str] = field(default_factory=dict)
    complexity_score: float = 0.0
    metadata: Dict = field(default_factory=dict)


@dataclass
class VerificationReport:
    """
    Verification results for educational quality.
    """
    accuracy_score: float
    simplicity_score: float
    passed: bool
    issues: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)


@dataclass
class EducationalPackage:
    """
    Final package produced by the educational pipeline.
    """
    concept: ConceptDefinition
    simplified: SimplifiedConcept
    verification: VerificationReport