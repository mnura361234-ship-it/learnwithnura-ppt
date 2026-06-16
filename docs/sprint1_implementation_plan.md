# Sprint 1 Implementation Plan

## Purpose
Define an execution plan for Sprint 1 that focuses only on the core educational modules and minimal risk delivery.

---

## Step 1: Finalize Models and Contracts

### Goal
Lock down the Sprint 1 domain models and stage contracts before coding.

### Files affected
- `docs/domain_models.md`
- `docs/pipeline_contracts.md`
- `docs/readiness_audit.md`
- `docs/sprint1_dependency_map.md`

### Dependencies
- Existing documentation in `docs/`.
- Input from the current repository and current stage contracts.

### Acceptance criteria
- Shared models are defined and consistent.
- Stage contracts are aligned across docs.
- Terminology is normalized.

### Testing approach
- Review documents with the implementation team.
- Validate that each model maps cleanly to module inputs/outputs.

### Estimated effort
- 1 day

---

## Step 2: Implement Concept Decomposer

### Goal
Build the first module that transforms raw concepts into a normalized concept definition.

### Files affected
- `learnwithnura-ppt/education/concept_decomposer.py`
- `docs/sprint1_dependency_map.md`
- `docs/domain_models.md`

### Dependencies
- `docs/domain_models.md`
- `parser.py` or text utilities for raw content processing
- `config.py` for any default metadata use

### Acceptance criteria
- The module accepts raw concept text and returns a `Concept` object.
- It marks `status` as `atomic` or `compound`.
- It emits explicit `prerequisites` and `analogyCategories`.

### Testing approach
- Unit tests for decomposing single concepts.
- Validation of `atomic` and `compound` cases.

### Estimated effort
- 2-3 days

---

## Step 3: Implement Simplification Engine

### Goal
Build the module that converts `Concept` objects to simplified text and glossary output.

### Files affected
- `learnwithnura-ppt/education/simplification_engine.py`
- `docs/domain_models.md`
- `docs/verification_rules_catalog.md`

### Dependencies
- `Concept` model from Step 1.
- simple text utilities in the repository.

### Acceptance criteria
- The module produces `SimplifiedConcept` objects.
- It enforces `averageSentenceLength <= 15`.
- It creates glossary entries for retained terms.

### Testing approach
- Unit tests for plain-language conversion.
- Edge case tests for fallback glossary creation.

### Estimated effort
- 3-4 days

---

## Step 4: Implement Verification Engine

### Goal
Build the module that evaluates simplified concepts against Sprint 1 verification rules.

### Files affected
- `learnwithnura-ppt/education/verification_engine.py`
- `docs/verification_rules_catalog.md`
- `docs/pipeline_contracts.md`

### Dependencies
- `SimplifiedConcept` model from Step 2.
- `VerificationReport` model from Step 1.

### Acceptance criteria
- The module returns a complete `VerificationReport`.
- It applies the defined threshold and completeness rules.
- It flags issues with clear recommendations.

### Testing approach
- Unit tests for rule enforcement.
- Test cases for pass/fail and issue generation.

### Estimated effort
- 3-4 days

---

## Step 5: Implement Pipeline Orchestrator

### Goal
Build the coordinating module that runs Sprint 1 stages in sequence and assembles the final package.

### Files affected
- `learnwithnura-ppt/education/pipeline_orchestrator.py`
- `docs/sprint1_dependency_map.md`
- `docs/domain_models.md`

### Dependencies
- Outputs from Steps 2-4.
- Simple orchestration code, no downstream modules.

### Acceptance criteria
- It calls Concept Decomposer, Simplification Engine, and Verification Engine in order.
- It assembles a valid `EducationalPackage`.
- It stops or returns revision instructions when verification fails.

### Testing approach
- Integration tests for full Sprint 1 flow.
- Mocked stage tests for orchestrator behavior.

### Estimated effort
- 2-3 days

---

## Step 6: Validate Sprint 1 Pipeline and Documentation

### Goal
Ensure the Sprint 1 pipeline is stable and ready for implementation handoff.

### Files affected
- `tests/` (new tests)
- `docs/readiness_audit.md`
- `docs/sprint1_dependency_map.md`
- `docs/repository_gap_report.md`

### Dependencies
- Completed code from Steps 2-5.
- Existing repository test conventions.

### Acceptance criteria
- All Sprint 1 unit and integration tests pass.
- Documentation is aligned with the implemented contracts.
- The readiness audit shows no unresolved critical issues.

### Testing approach
- Execute unit tests for each module.
- Run an end-to-end sample concept through the orchestrator.

### Estimated effort
- 2 days

---

## Sprint 1 Notes
- Do not implement `Analogy`, `VisualExplanation`, `HausaLocalization`, or `OutputRenderer` in this sprint.
- Keep the orchestrator contract limited to Sprint 1 stage outputs.
- Use the current repository as a stable foundation, adding only the `education/` package and test scaffolding.
