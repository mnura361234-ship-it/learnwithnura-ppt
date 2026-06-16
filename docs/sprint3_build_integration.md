# Sprint 3: Build Integration — Presentation Adapter

**Date:** 2026-06-16

## Overview

Sprint 3 connects the Education Pipeline to the existing LearnWithNura build system. The new `PresentationAdapter` converts raw slide dictionaries (from `SlideBuilder`) into the textual `slides.txt` format the Presentation Engine already consumes. The integration is performed at the orchestration level by extending `EducationalPipeline` with a non-breaking `generate_presentation()` convenience method that ultimately calls into `build.run_build()`.

## Architecture Before

Topic → Decomposer → Simplifier → Verifier → EducationalPackage → SlideBuilder → [stopped]

## Architecture After

Topic → Decomposer → Simplifier → Verifier → EducationalPackage → SlideBuilder → PresentationAdapter → Build System (`build.py`) → Presentation Engine (`generate.py`) → `.pptx`

## Files Added

- `education/presentation_adapter/__init__.py` — exports `PresentationAdapter`.
- `education/presentation_adapter/presentation_adapter.py` — converts SlideBuilder output into `slides.txt` format and persists it using `content_manager.save_to_slides()`.
- `education/examples/generate_demo.py` — example demonstrating `pipeline.generate_presentation()`.
- `education/tests/test_presentation_adapter.py` — unit tests for the adapter conversion.
- `education/tests/test_generate_presentation.py` — integration test for the `generate_presentation()` API.

## Files Modified

- `education/pipeline/orchestrator.py` — added import of `PresentationAdapter`, instantiated it, and added `generate_presentation()` method which:
  1. Runs `self.run(concept)` to produce an `EducationalPackage`.
  2. Builds slides via `SlideBuilder`.
  3. Calls `PresentationAdapter.prepare(slides)` to write `slides.txt`.
  4. Invokes `build.run_build()` to trigger the regular build → generate workflow.
  5. Returns the final output path from `project_manager.get_output_path()`.

## Why the Build System

- `build.py` is the canonical orchestration layer already used by producers and the CLI. Integrating at this level preserves the existing developer experience and avoids duplicating orchestration logic.
- `generate.py` remains untouched and solely responsible for rendering.

## Usage

High-level convenience API:

```python
from education.pipeline.orchestrator import EducationalPipeline

pipeline = EducationalPipeline()
output_path = pipeline.generate_presentation("Artificial Intelligence")
print("Generated presentation:", output_path)
```

Command-line build remains unchanged:

```bash
python build.py
```

## Testing

Run:

```bash
python -m compileall -q .
python -m unittest discover -v
```

All tests pass (including the new education tests).

## Future Work

- Add options to `generate_presentation()` to select templates or override presentation metadata.
- Add more sophisticated slide mapping (e.g., mapping glossary terms into a dedicated glossary slide).
- Support direct in-memory invocation of `generate.py` with slide structures for faster CI cycles.

---

Sprint 3 preserves architecture and provides a clean, backward-compatible path from `Topic` to `.pptx`.
