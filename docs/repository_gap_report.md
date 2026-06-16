# Repository Gap Report

## Purpose
Compare the current repository structure against the `repository_evolution_plan.md` recommended structure and identify gaps for Sprint 1.

---

## Existing Repository Structure

### Current directories
- `assets/`
- `backups/`
- `blueprints/`
- `components/`
- `layouts/`
- `output/`
- `prompts/`
- `providers/`
- `templates/`
- `tests/`
- `themes/`

### Current top-level files
- `assets_manager.py`
- `backup_manager.py`
- `build.py`
- `config.py`
- `content_manager.py`
- `developer_tools.py`
- `generate.py`
- `icon_manager.py`
- `image_manager.py`
- `parser.py`
- `project_manager.py`
- `README.md`
- `slides.txt`
- `topics.json`
- `utils.py`
- `version.py`

---

## Required Sprint 1 Structure

The evolution plan recommends a new education package and integration support.

### Required folders and files
- `learnwithnura-ppt/education/`
  - `__init__.py`
  - `concept_decomposer.py`
  - `simplification_engine.py`
  - `verification_engine.py`
  - `pipeline_orchestrator.py`
- `learnwithnura-ppt/education/output_renderer_adapter.py` (future integration)

### Required integrations
- `build.py` must support an educational pipeline or orchestrator entry.
- `config.py` should allow optional educational pipeline configuration.
- `project_manager.py` should include validation for new educational stage requirements.
- `README.md` should document the Sprint 1 educational pipeline if implemented.

---

## Missing Folders
- `learnwithnura-ppt/education/`
- `learnwithnura-ppt/education/__init__.py`

## Missing Interfaces
- Educational pipeline mode in `build.py`.
- `education` package support in `config.py`.
- Validation or support hooks in `project_manager.py` for education artifacts.
- `output_renderer_adapter.py` for translating future package output.

## Migration Requirements

### 1. Add an education package
- Create `learnwithnura-ppt/education/` as a new package.
- Add Sprint 1 modules inside that package.
- Keep the package isolated from existing slide-generation code.

### 2. Preserve existing build behavior
- Do not change current provider/generation workflows until Sprint 1 educational pipeline is validated.
- Add a separate educational entry point instead of replacing the existing generator.

### 3. Keep repository contracts explicit
- Define new config settings only if necessary.
- Avoid introducing untested build or project-manager logic in Sprint 1.

---

## Suggested Implementation Sequence

1. **Create the education package scaffold**
   - `education/__init__.py`
   - `concept_decomposer.py`
   - `simplification_engine.py`
   - `verification_engine.py`
   - `pipeline_orchestrator.py`

2. **Implement stage contracts and models**
   - Use `docs/domain_models.md` and `docs/pipeline_contracts.md`.

3. **Keep build integration minimal**
   - Defer `build.py` educational mode until the pipeline is stable.
   - For Sprint 1, prefer direct execution via `education/pipeline_orchestrator.py`.

4. **Add tests and validation**
   - Place unit tests in `tests/`.
   - Add an end-to-end sample concept test for Sprint 1.

5. **Document the Sprint 1 boundary**
   - Record the gap between current repo state and the new education package.
   - Keep future adapter work separate from Sprint 1 delivery.

---

## Gap Summary
The current repository supports a slide-generation engine but does not yet contain the recommended Sprint 1 educational package or the integration points described in `repository_evolution_plan.md`. The gap is structural and should be addressed through a minimal, isolated `education/` package plus a narrow orchestration entry point.

## Documentation Alignment Status
- Sprint 1 contract and shared model documents have been reviewed and aligned to use `ConceptDefinition`, `SimplifiedConcept`, and `VerificationReport` consistently.
- The repository gap remains implementation-focused: the docs are now consistent, but the actual `education/` package scaffold is still missing.
