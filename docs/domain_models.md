# Domain Model Design

## Purpose
Define the core data models for the Sprint 1 educational pipeline without implementing code. These models should be the basis for module contracts and tests.

---

## Model: Concept

### Fields
- `conceptId`: string
- `title`: string
- `statement`: string
- `scope`: string
- `status`: string (`atomic` | `compound`)
- `prerequisites`: array[string]
- `analogyCategories`: array[string]
- `decompositionNotes`: string
- `metadata`: object
  - `rawLength`: integer
  - `domainTags`: array[string]
  - `sourceReference`: string (optional)

### Required attributes
- `conceptId`
- `title`
- `statement`
- `scope`
- `status`

### Optional attributes
- `prerequisites`
- `analogyCategories`
- `decompositionNotes`
- `metadata.sourceReference`

### Validation rules
- `statement` must be non-empty.
- `status` must be `atomic` or `compound`.
- `scope` must be explicit and actionable.
- `analogyCategories` should contain at least one category when available.
- `prerequisites` may be empty, but if the concept depends on prior knowledge, the list must be explicit.

### Relationships
- A `Concept` is the input to `SimplifiedConcept`.
- `Prerequisite` values are derived from `Concept.prerequisites`.

---

## Model: Prerequisite

### Fields
- `text`: string
- `type`: string (optional)
- `referenceId`: string (optional)

### Required attributes
- `text`

### Optional attributes
- `type`
- `referenceId`

### Validation rules
- `text` must be clear and specific.
- If `type` is provided, it must be meaningful (e.g. `concept`, `skill`, `term`).

### Relationships
- `Prerequisite` items appear within a `Concept` definition.
- They may also be referenced indirectly by verification rules.

---

## Model: SimplifiedConcept

### Fields
- `conceptId`: string
- `simplifiedText`: string
- `glossary`: array[GlossaryTerm]
- `complexityScore`: integer
- `simplificationMetadata`: object
  - `sentenceCount`: integer
  - `averageSentenceLength`: float
  - `retainedTechnicalTerms`: array[string]
- `originalConcept`: Concept (optional)

### Required attributes
- `conceptId`
- `simplifiedText`
- `glossary`
- `complexityScore`
- `simplificationMetadata`

### Optional attributes
- `originalConcept`

### Validation rules
- `simplifiedText` must be present.
- `averageSentenceLength` must be ≤ 15.
- `glossary` must define any retained technical terms.
- `complexityScore` must be an integer between 0 and 100.
- `sentenceCount` must be consistent with `simplifiedText`.

### Relationships
- `SimplifiedConcept` is produced from `Concept`.
- It is consumed by `VerificationReport` and later by analogy/visual modules.

---

## Model: VerificationReport

### Fields
- `conceptId`: string
- `accuracyScore`: integer
- `simplicityScore`: integer
- `analogyNeed`: boolean
- `visualNeed`: boolean
- `passStatus`: boolean
- `issues`: array[Issue]
- `verificationMetadata`: object
  - `timestamp`: string
  - `reviewerNotes`: string
- `finalScore`: integer (optional)
- `recommendationLevel`: string (optional)
- `revisionCount`: integer (optional)

### Required attributes
- `conceptId`
- `accuracyScore`
- `simplicityScore`
- `analogyNeed`
- `visualNeed`
- `passStatus`
- `issues`
- `verificationMetadata`

### Optional attributes
- `finalScore`
- `recommendationLevel`
- `revisionCount`

### Validation rules
- All required numeric scores must be between 0 and 100.
- `passStatus` must be boolean.
- `issues` may be empty, but if any issue exists, it must contain `issueId`, `category`, `severity`, and `description`.
- `finalScore`, when present, must be computed from the score dimensions.

### Relationships
- `VerificationReport` is attached to a `SimplifiedConcept`.
- It is incorporated into the final `EducationalPackage`.

---

## Model: Analogy

### Fields
- `conceptId`: string
- `analogyText`: string
- `analogyType`: string
- `analogyMappingNotes`: string
- `analogyScore`: integer

### Required attributes
- `conceptId`
- `analogyText`
- `analogyType`

### Optional attributes
- `analogyMappingNotes`
- `analogyScore`

### Validation rules
- `analogyText` must be non-empty.
- `analogyType` must match one of the selected analogy categories.
- `analogyScore`, when present, must be between 0 and 100.

### Relationships
- `Analogy` is derived from a verified `SimplifiedConcept`.
- It is a future input to `VisualSpecification` and `LocalizationPackage`.

---

## Model: VisualSpecification

### Fields
- `conceptId`: string
- `visualType`: string
- `entities`: array[string]
- `relationships`: array[string]
- `labels`: array[string]
- `layoutGuidelines`: string
- `visualScore`: integer

### Required attributes
- `conceptId`
- `visualType`
- `entities`
- `relationships`

### Optional attributes
- `labels`
- `layoutGuidelines`
- `visualScore`

### Validation rules
- `visualType` must be a supported visual form.
- `entities` and `relationships` must not be empty.
- `visualScore`, when present, must be between 0 and 100.

### Relationships
- `VisualSpecification` is a downstream artifact of `Analogy` and `SimplifiedConcept`.
- It supports future rendering operations.

---

## Model: LocalizationPackage

### Fields
- `conceptId`: string
- `hausaText`: string
- `hausaAnalogy`: string
- `terminologyNotes`: array[TermNote]
- `localizationScore`: integer

### Required attributes
- `conceptId`
- `hausaText`

### Optional attributes
- `hausaAnalogy`
- `terminologyNotes`
- `localizationScore`

### Validation rules
- `hausaText` must preserve the meaning of the simplified concept.
- `localizationScore`, when present, must be between 0 and 100.
- `terminologyNotes` should document any retained technical terms.

### Relationships
- `LocalizationPackage` is consumed by the final `EducationalPackage`.

---

## Model: EducationalPackage

### Fields
- `conceptId`: string
- `simplifiedConcept`: SimplifiedConcept
- `verificationReport`: VerificationReport
- `analogy`: Analogy (optional)
- `visualSpecification`: VisualSpecification (optional)
- `localizationPackage`: LocalizationPackage (optional)
- `packageStatus`: string

### Required attributes
- `conceptId`
- `simplifiedConcept`
- `verificationReport`
- `packageStatus`

### Optional attributes
- `analogy`
- `visualSpecification`
- `localizationPackage`

### Validation rules
- `packageStatus` must be `ready`, `revision`, or `incomplete`.
- The package must include at least `simplifiedConcept` and `verificationReport` for Sprint 1.
- Optional downstream artifacts may be absent in Sprint 1.

### Relationships
- `EducationalPackage` is the assembled output of the Sprint 1 pipeline.
- It may later expand to include analogy, visual, and localization artifacts.
