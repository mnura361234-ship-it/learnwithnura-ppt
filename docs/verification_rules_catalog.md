# Verification Rules Catalog

## Purpose
Convert LearnWithNura educational quality requirements into machine-checkable rules for Sprint 1.

---

## Rule: Atomic Unit Rule

### Purpose
Ensure each concept is a single, teachable learning unit.

### Detection method
- Inspect `Concept.status`.
- Analyze `Concept.statement` for multiple distinct ideas or compound clauses.

### Pass criteria
- `Concept.status == "atomic"`
- `Concept.statement` contains one primary idea or mechanism.

### Failure criteria
- `Concept.status == "compound"`
- `Concept.statement` clearly contains more than one core concept.

### Severity
- critical

### Recommended fix
Split the concept into separate atomic concepts or create explicit prerequisites for dependent ideas.

---

## Rule: Jargon Minimalism Rule

### Purpose
Prevent unexplained technical terms from remaining in simplified content.

### Detection method
- Scan `SimplifiedConcept.simplifiedText` for retained technical terms.
- Compare retained terms against `SimplifiedConcept.glossary`.

### Pass criteria
- All retained technical terms are defined in `glossary`.
- No specialist terms remain unexplained.

### Failure criteria
- A technical term appears in `simplifiedText` without an entry in `glossary`.
- The simplified text contains jargon that is not replaced or defined.

### Severity
- major

### Recommended fix
Replace jargon with plain language or add a glossary entry for each retained term.

---

## Rule: 10-Year-Old Rule

### Purpose
Ensure content remains readable and accessible at a child-friendly level.

### Detection method
- Calculate `simplificationMetadata.averageSentenceLength`.
- Optionally check sentence count and sentence structure complexity.

### Pass criteria
- `averageSentenceLength <= 15`

### Failure criteria
- `averageSentenceLength > 15`

### Severity
- major

### Recommended fix
Split long sentences, remove nested clauses, and simplify phrasing.

---

## Rule: Analogy Anchor Rule

### Purpose
Ensure analogies are relevant and structurally linked to the concept.

### Detection method
- Verify `Analogy.analogyText` is non-empty.
- Confirm `Analogy.analogyType` is one of the selected categories.
- Check `Analogy.analogyScore` if available.

### Pass criteria
- `analogyText` is provided.
- `analogyType` matches a category from the concept.
- `analogyScore >= 70` when a score is present.

### Failure criteria
- `analogyText` is missing.
- `analogyType` is invalid for the concept.
- `analogyScore` is below 70.

### Severity
- major

### Recommended fix
Choose a better analogy category and ensure the analogy maps directly to the concept structure.

---

## Rule: Visual Structural Rule

### Purpose
Ensure visual specifications represent concept entities and relationships clearly.

### Detection method
- Inspect `VisualSpecification.entities` and `VisualSpecification.relationships`.
- Confirm `visualType` is supported.
- Check `visualScore` when present.

### Pass criteria
- `entities` and `relationships` are non-empty.
- `visualType` is a supported visual form.
- `visualScore >= 70` when a score is present.

### Failure criteria
- Missing or empty entity and relationship lists.
- Unsupported `visualType`.
- `visualScore` below threshold.

### Severity
- major

### Recommended fix
Define the visual structure explicitly and choose a supported visualization pattern.

---

## Rule: Prerequisite Transparency Rule

### Purpose
Make all required prior knowledge explicit rather than implied.

### Detection method
- Inspect `Concept.prerequisites`.
- Review `SimplifiedConcept.simplifiedText` for hidden assumptions.

### Pass criteria
- If the concept depends on prior ideas, `prerequisites` is non-empty.
- If no prerequisites are needed, the list is intentionally empty and the concept is self-contained.

### Failure criteria
- The concept appears to require prior knowledge but prerequisites are missing.
- The simplified text assumes familiarity with undefined ideas.

### Severity
- major

### Recommended fix
Add missing prerequisite entries or simplify the concept further so it no longer depends on hidden knowledge.

---

## Rule: Verification Report Completeness Rule

### Purpose
Ensure the verification report contains the required fields for downstream decision making.

### Detection method
- Inspect `VerificationReport` payload.
- Confirm required fields are present.

### Pass criteria
- `conceptId`, `accuracyScore`, `simplicityScore`, `analogyNeed`, `visualNeed`, `passStatus`, `issues`, and `verificationMetadata` are present.

### Failure criteria
- Any required field is missing.
- `issues` is absent or malformed.

### Severity
- critical

### Recommended fix
Populate the missing fields and ensure the report schema matches the contract.
