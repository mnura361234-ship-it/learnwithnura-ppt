# Build Execution Plan

## Purpose
This document defines the implementation-ready build and execution plan for the LearnWithNura educational core. It maps the work into concrete tasks, phases, and deliverables.

---

## Phase 1: Prepare Architecture and Scoping

### Goals
- Lock down the MVP architecture
- Define module contracts and pipeline rules
- Prepare repository evolution plan

### Deliverables
- `docs/architecture_decision_record.md`
- `docs/final_module_catalog.md`
- `docs/mvp_specification.md`
- `docs/pipeline_contracts.md`
- `docs/verification_system_design.md`
- `docs/repository_evolution_plan.md`

### Action Items
- Review and finalize the eight core educational modules
- Confirm implementation scope with the existing repository foundation
- Document interface contracts for each stage

---

## Phase 2: Implement Core Modules

### Goals
- Build the eight MVP educational modules
- Keep the implementation bounded and testable

### Deliverables
- New `learnwithnura-ppt/education/` package
- `concept_decomposer.py`
- `simplification_engine.py`
- `verification_engine.py`
- `analogy_engine.py`
- `visual_explanation_engine.py`
- `hausa_localization_engine.py`
- `pipeline_orchestrator.py`
- `output_renderer_adapter.py`

### Action Items
- Implement each module with clear input/output contracts
- Use the existing codebase for parser, theme, and output support
- Keep each module unit-testable

---

## Phase 3: Integrate and Connect

### Goals
- Wire the new educational pipeline into the current generation workflow
- Create a thin adapter from the `FinalPackage` into existing slide output

### Deliverables
- Updated `build.py` with educational pipeline mode
- Integration adapter between `pipeline_orchestrator` and current renderer
- Minimal CLI/config support for educational mode

### Action Items
- Add pipeline entry points to `generate.py` or `build.py`
- Ensure the educational output can be rendered with current slide templates
- Preserve existing presentation engine fallback

---

## Phase 4: Test and Validate

### Goals
- Ensure pipeline behavior is correct and reliable
- Validate end-to-end package generation

### Deliverables
- Unit tests for all new education modules
- Integration tests for pipeline execution
- Verification tests for pass/fail logic

### Action Items
- Add tests under `tests/` following existing conventions
- Build a sample concept end-to-end test
- Validate output consistency with current renderer

---

## Phase 5: Document and Stabilize

### Goals
- Make the new architecture discoverable
- Ensure maintainers understand the implementation path

### Deliverables
- `README.md` updates describing the education pipeline
- docs references from `docs/architecture.md` and `docs/development_rules.md`
- Updated module boundaries and future extension notes

### Action Items
- Add a short architecture summary to `README.md`
- Ensure docs point to the new `education/` package
- Capture any implementation notes in `docs/architecture.md`

---

## Phase 6: Future Readiness

### Goals
- Preserve a clean extension path for later phases
- Avoid coupling the core pipeline to non-essential systems

### Deliverables
- `docs/repository_evolution_plan.md`
- explicit extension points in `pipeline_orchestrator.py`
- stable module contracts in `docs/pipeline_contracts.md`

### Action Items
- Define extension points for strategy, multi-format output, and reviews
- Keep the core educational pipeline isolated from social/analytics systems
- Plan next-phase work only after MVP stabilization

---

## Execution Notes

### Solo Developer Focus
- Work sequentially through the eight core modules.
- Avoid introducing new infrastructure beyond the necessary educational layer.
- Keep documentation current with every implementation step.

### Risk Mitigation
- Use the existing repository’s current output engine as an adapter boundary.
- Maintain backward compatibility by keeping existing output paths intact.
- Defer all non-core modules until after the MVP is stable.

### Tracking
- Treat each module as a milestone.
- Use the verification system design as the core acceptance authority.
- Track progress by implementation of stage contracts and passing tests.
