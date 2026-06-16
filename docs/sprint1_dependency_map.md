# Sprint 1 Dependency Map

## Scope
Sprint 1 modules:
- Concept Decomposer
- Simplification Engine
- Verification Engine
- Pipeline Orchestrator

These modules implement the first usable educational pipeline and prepare the system for future analogy, visual, and localization stages.

---

## Shared Models
- `Concept` / `ConceptDefinition`
- `Prerequisite`
- `SimplifiedConcept`
- `VerificationReport`
- `EducationalPackage`

These shared models are the contract layer between modules; they must be defined before implementation begins.

---

## Module Dependencies

### 1. Concept Decomposer
- Inputs:
  - raw concept statement
  - domain tags
  - learner profile
  - optional source reference
- Outputs:
  - conceptId
  - title
  - statement
  - scope
  - prerequisites
  - recommended analogy categories
  - conceptStatus (`atomic` / `compound`)
  - metadata
- Shared models:
  - `Concept`
  - `Prerequisite`
- Required interfaces:
  - `decompose(rawConcept, context) -> ConceptDefinition`

### 2. Simplification Engine
- Inputs:
  - `ConceptDefinition`
  - prerequisite list
  - learner profile
- Outputs:
  - simplifiedText
  - glossary
  - complexityScore
  - simplificationMetadata
- Shared models:
  - `SimplifiedConcept`
- Required interfaces:
  - `simplify(conceptDefinition) -> SimplifiedConcept`

### 3. Verification Engine
- Inputs:
  - `SimplifiedConcept`
  - glossary
  - complexityScore
  - conceptId
- Outputs:
  - `VerificationReport`
  - pass/fail status
  - issues list
- Shared models:
  - `VerificationReport`
- Required interfaces:
  - `verify(simplifiedConcept) -> VerificationReport`

### 4. Pipeline Orchestrator
- Inputs:
  - raw concept input package
  - pipeline metadata
  - execution configuration
- Outputs:
  - `EducationalPackage`
  - stage status metadata
  - revision instructions
- Shared models:
  - `ConceptDefinition`
  - `SimplifiedConcept`
  - `VerificationReport`
  - `EducationalPackage`
- Required interfaces:
  - `runPipeline(rawConceptPackage) -> FinalPackage`

---

## Execution Order

1. Concept Decomposer
2. Simplification Engine
3. Verification Engine
4. Pipeline Orchestrator (orchestrates and assembles outputs)

### Simplified flow diagram

```
[RawConceptInput]
        |
        v
[Concept Decomposer] -- produces --> [ConceptDefinition]
        |
        v
[Simplification Engine] -- produces --> [SimplifiedConcept]
        |
        v
[Verification Engine] -- produces --> [VerificationReport]
        |
        v
[Pipeline Orchestrator] -- produces --> [EducationalPackage]
```

### Orchestrator role
The Pipeline Orchestrator is the coordinator, not a data transformer itself. In Sprint 1 it should:
- call the Concept Decomposer,
- call the Simplification Engine,
- call the Verification Engine,
- assemble the final package,
- enforce pass/fail gating.

---

## Required Interfaces

- `ConceptDecomposer.decompose(rawConcept, learnerProfile, domainTags, sourceReference?) -> ConceptDefinition`
- `SimplificationEngine.simplify(conceptDefinition) -> SimplifiedConcept`
- `VerificationEngine.verify(simplifiedConcept) -> VerificationReport`
- `EducationalPipeline.run(rawConceptPackage) -> EducationalPackage`

---

## Future Integration Points

- `Analogy Engine` will consume `Verified SimplifiedConcept` and `recommendedAnalogyCategories`.
- `Visual Explanation Engine` will consume `Verified SimplifiedConcept` and `AnalogyPackage`.
- `Hausa Localization Engine` will consume final verified content and visual specification.
- `Output Renderer` will consume `EducationalPackage` and produce slide/presentation artifacts.

### Future diagram extension

```
[Verification Report] --> [Analogy Engine] --> [Visual Engine] --> [Localization Engine] --> [Output Renderer]
```

---

## Sprint 1 Risk Notes
- Keep the orchestrator contract intentionally simple for Sprint 1.
- Do not require analogy, visual, or localization models until Sprint 2.
- Define shared models early to avoid naming drift across docs and code.
