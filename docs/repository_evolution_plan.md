# Repository Evolution Plan

## Purpose
This document defines the recommended repository structure and evolution plan for implementing the LearnWithNura educational core while preserving the existing foundation.

---

## Current Repository Foundation
The current repository already contains:
- content generation engine
- layouts and components
- theme definitions
- provider registry
- prompt templates
- output renderer for slides
- tests for core modules

This plan preserves those foundations and layers the new educational core on top.

---

## Evolution Strategy

### Phase 1: Core Educational Layer
Add the new educational modules without changing existing renderer or theme behavior.

New directories and files:
- `learnwithnura-ppt/education/`
  - `__init__.py`
  - `concept_decomposer.py`
  - `simplification_engine.py`
  - `verification_engine.py`
  - `analogy_engine.py`
  - `visual_explanation_engine.py`
  - `hausa_localization_engine.py`
  - `pipeline_orchestrator.py`
  - `output_renderer_adapter.py`

### Phase 2: Integration with Existing Pipeline
Integrate the educational core into the existing generator and build workflow.
- Update `build.py` to add an educational pipeline mode.
- Add `education` support to `config.py` and `project_manager.py` as needed.
- Keep existing PowerPoint output code intact while creating a thin adapter to the new `output_renderer_adapter.py`.

### Phase 3: Repository Cleanup and Discoverability
- Add `education` package to `__init__.py` exports if needed.
- Add module discovery to `provider_registry.py` or a dedicated education registry.
- Update `README.md` to describe the new educational pipeline and developer workflow.

### Phase 4: Tests and Documentation
- Add unit tests for each new educational module under `tests/`.
- Add integration tests for the pipeline end-to-end.
- Add docs for pipeline contracts and module responsibilities.

---

## Recommended Directory Structure

Root-level modules should remain stable; new education modules live in a dedicated package.

- `learnwithnura-ppt/`
  - `education/`
    - `__init__.py`
    - `concept_decomposer.py`
    - `simplification_engine.py`
    - `verification_engine.py`
    - `analogy_engine.py`
    - `visual_explanation_engine.py`
    - `hausa_localization_engine.py`
    - `pipeline_orchestrator.py`
    - `output_renderer_adapter.py`
  - `content_manager.py`
  - `generate.py`
  - `build.py`
  - `config.py`
  - `project_manager.py`

---

## Integration Points

### Existing Infrastructure
- `generate.py` and `content_manager.py` should remain the rendering engine boundary.
- The new education pipeline should emit structured packages that existing slide generation can render.
- The theme and layout registry remain the visual presentation foundation.

### New Boundary
- `pipeline_orchestrator.py` becomes the primary entry point for educational package creation.
- `output_renderer_adapter.py` translates `FinalPackage` objects into slide-compatible payloads.

---

## Migration Rules
- Implement new modules incrementally.
- Avoid changing existing `themes/`, `layouts/`, or `components/` unless required by the adapter.
- Keep old generator behavior available as a fallback during early development.

---

## Validation Plan
- Start with unit tests for each educational module.
- Add end-to-end tests that verify a raw concept passes through all stages and produces a final render result.
- Use current test conventions in `tests/` to keep coverage consistent.

---

## Future Evolution
After the educational core is stable, evolve the repository with:
- `education/strategy/`
- `education/multi_format/`
- `education/feedback/`
- `education/localization/`
- `education/platforms/`

This plan preserves the current codebase while enabling future educational extension.
