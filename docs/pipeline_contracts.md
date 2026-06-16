# Pipeline Contracts

## Purpose
This document defines explicit contracts for each stage of the LearnWithNura educational pipeline. It is the authoritative reference for data shapes, validation rules, failure conditions, pass conditions, and required metadata.

---

## Stage 1: Concept Decomposition

### Input Schema
- `rawConceptId`: string
- `rawConceptText`: string
- `domainTags`: array[string]
- `learnerProfile`: object
  - `experienceLevel`: string
  - `language`: string
- `sourceReference`: string (optional)

### Output Schema
- `conceptDefinition`: object
  - `conceptId`: string
  - `title`: string
  - `statement`: string
  - `scope`: string
  - `status`: enum[atomic, compound]
  - `prerequisites`: array[string]
  - `analogyCategories`: array[string]
  - `decompositionNotes`: string
  - `metadata`: object
    - `rawLength`: integer
    - `domainTags`: array[string]
    - `sourceReference`: string (optional)

This stage produces the canonical `ConceptDefinition` model for Sprint 1.

### Validation Rules
- `conceptStatement` must be non-empty
- `prerequisites` may be empty but should exist
- `conceptStatus` must equal `atomic` or `compound`
- `recommendedAnalogyCategories` must contain at least one value

### Failure Conditions
- Empty or ambiguous `conceptStatement`
- `conceptStatus` missing or invalid
- No recommended analogy category

### Pass Conditions
- valid `conceptId`
- atomic or compound status assigned correctly
- prerequisites identified or explicitly marked empty
- concept scope clearly defined

### Required Metadata
- `rawLength`
- `domainTags`
- source provenance if available

---

## Stage 2: Simplification

### Input Schema
- `conceptDefinition`: object
- `prerequisites`: array[string]
- `learnerProfile`: object

### Output Schema
- `simplifiedText`: string
- `glossary`: array[object]
  - `term`: string
  - `definition`: string
- `complexityScore`: integer (0-100)
- `simplificationMetadata`: object
  - `sentenceCount`: integer
  - `averageSentenceLength`: float
  - `retainedTechnicalTerms`: array[string]

### Validation Rules
- `simplifiedText` must be shorter than the original `conceptDefinition.statement`
- `averageSentenceLength` must be ≤ 15
- `complexityScore` must be computed and included
- `retainedTechnicalTerms` must be defined in the `glossary`

### Failure Conditions
- undefined technical terms remain in simplifiedText
- average sentence length > 15
- complexityScore is missing

### Pass Conditions
- clear simplified explanation
- glossary present for retained terms
- complexityScore and metadata valid

### Required Metadata
- `sentenceCount`
- `averageSentenceLength`
- `complexityScore`

---

## Stage 3: Verification

### Input Schema
- `simplifiedConcept`: object
  - `conceptId`: string
  - `simplifiedText`: string
  - `glossary`: array[object]
  - `complexityScore`: integer
  - `simplificationMetadata`: object
- `conceptDefinition`: object
- `sourceReference`: string (optional)

### Output Schema
- `verificationReport`: object
  - `conceptId`: string
  - `accuracyScore`: integer
  - `simplicityScore`: integer
  - `analogyNeed`: boolean
  - `visualNeed`: boolean
  - `passStatus`: boolean
  - `issues`: array[object]
  - `finalScore`: integer
  - `recommendationLevel`: string
  - `revisionCount`: integer
  - `generatedAt`: string
- `verificationMetadata`: object
  - `timestamp`: string
  - `reviewerNotes`: string

### Validation Rules
- `conceptId`, `accuracyScore`, `simplicityScore`, `finalScore`, `recommendationLevel`, and `generatedAt` must be present
- `passStatus` true only if all required thresholds are met
- `issues` must document any reasons for failure
- `finalScore` must be computed from score dimensions

### Failure Conditions
- undefined technical terms remain in simplifiedText
- average sentence length > 15
- complexityScore is missing

### Pass Conditions
- clear simplified explanation
- glossary present for retained terms
- complexityScore and metadata valid

### Required Metadata
- `sentenceCount`
- `averageSentenceLength`
- `complexityScore`

---

## Stage 4: Visualization

### Input Schema
- `simplifiedText`: string
- `analogyText`: string
- `conceptStructure`: object

### Output Schema
- `visualType`: string
- `visualSpec`: object
  - `entities`: array[string]
  - `relationships`: array[string]
  - `labels`: array[string]
  - `layoutGuidelines`: string
- `visualScore`: integer

### Validation Rules
- `visualType` must be one of the supported visual forms
- `visualSpec` must include entities and relationships
- `visualScore` must be computed

### Failure Conditions
- missing entities or relationships
- visualType unsupported
- visualScore below threshold

### Pass Conditions
- complete `visualSpec`
- visualScore ≥ threshold
- alignment with simplifiedText and analogy

### Required Metadata
- `visualType`
- `visualScore`

---

## Stage 5: Localization

### Input Schema
- `simplifiedText`: string
- `analogyText`: string
- `visualSpec`: object
- `conceptId`: string

### Output Schema
- `hausaText`: string
- `hausaAnalogy`: string
- `terminologyNotes`: array[object]
- `localizationScore`: integer

### Validation Rules
- `hausaText` must preserve original meaning
- `hausaAnalogy` must be culturally relevant
- technical terms must be documented in `terminologyNotes`
- `localizationScore` must be present

### Failure Conditions
- meaning loss in Hausa text
- cultural mismatch in analogy
- missing terminology notes

### Pass Conditions
- Hausa package complete
- localizationScore ≥ threshold

### Required Metadata
- `localizationScore`
- `terminologyNotes`

---

## Stage 6: Package Assembly

### Input Schema
- `simplifiedText`: string
- `glossary`: array[object]
- `verificationReport`: object
- `analogyText`: string
- `visualSpec`: object
- `hausaText`: string
- `localizationScore`: integer
- `conceptId`: string

### Output Schema
- `finalPackage`: object
  - `conceptId`: string
  - `simplifiedText`: string
  - `glossary`: array[object]
  - `verificationReport`: object
  - `analogyText`: string
  - `visualSpec`: object
  - `hausaText`: string
  - `localizationScore`: integer
  - `packageStatus`: string

### Validation Rules
- all required outputs must be present
- `packageStatus` must indicate readiness or revision
- `finalPackage` must include all stage outputs

### Failure Conditions
- missing any required content block
- package status not set

### Pass Conditions
- full package assembled
- packageStatus = `ready`

### Required Metadata
- `packageStatus`
- `conceptId`

---

## Stage 7: Final Verification Gate

### Input Schema
- `finalPackage`: object
- `finalReviewMetadata`: object

### Output Schema
- `finalVerificationReport`: object
  - `finalScore`: integer
  - `passStatus`: boolean
  - `observations`: array[string]

### Validation Rules
- verify all package sections are present
- compute final aggregated score
- determine pass/fail based on threshold

### Failure Conditions
- missing package sections
- finalScore below threshold
- unresolved observations

### Pass Conditions
- passStatus true
- finalScore ≥ threshold
- no critical observations

### Required Metadata
- `finalScore`
- `passStatus`
- `observations`

### Input Schema
- `simplifiedText`: string
- `analogyText`: string
- `visualSpec`: object
- `conceptId`: string

### Output Schema
- `hausaText`: string
- `hausaAnalogy`: string
- `terminologyNotes`: array[object]
- `localizationScore`: integer

### Validation Rules
- `hausaText` must preserve original meaning
- `hausaAnalogy` must be culturally relevant
- technical terms must be documented in `terminologyNotes`
- `localizationScore` must be present

### Failure Conditions
- meaning loss in Hausa text
- cultural mismatch in analogy
- missing terminology notes

### Pass Conditions
- Hausa package complete
- localizationScore ≥ threshold

### Required Metadata
- `localizationScore`
- `terminologyNotes`

---

## Stage 8: Package Assembly

### Input Schema
- `simplifiedText`: string
- `glossary`: array[object]
- `verificationReport`: object
- `analogyText`: string
- `visualSpec`: object
- `hausaText`: string
- `localizationScore`: integer
- `conceptId`: string

### Output Schema
- `finalPackage`: object
  - `conceptId`: string
  - `simplifiedText`: string
  - `glossary`: array[object]
  - `verificationReport`: object
  - `analogyText`: string
  - `visualSpec`: object
  - `hausaText`: string
  - `localizationScore`: integer
  - `packageStatus`: string

### Validation Rules
- all required outputs must be present
- `packageStatus` must indicate readiness or revision
- `finalPackage` must include all stage outputs

### Failure Conditions
- missing any required content block
- package status not set

### Pass Conditions
- full package assembled
- packageStatus = `ready`

### Required Metadata
- `packageStatus`
- `conceptId`

---

## Stage 9: Final Verification Gate

### Input Schema
- `finalPackage`: object
- `finalReviewMetadata`: object

### Output Schema
- `finalVerificationReport`: object
  - `finalScore`: integer
  - `passStatus`: boolean
  - `observations`: array[string]

### Validation Rules
- verify all package sections are present
- compute final aggregated score
- determine pass/fail based on threshold

### Failure Conditions
- missing package sections
- finalScore below threshold
- unresolved observations

### Pass Conditions
- passStatus true
- finalScore ≥ threshold
- no critical observations

### Required Metadata
- `finalScore`
- `passStatus`
- `observations`
