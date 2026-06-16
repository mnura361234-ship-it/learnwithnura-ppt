# LearnWithNura Visual Education OS

This repository is evolving from a presentation engine into a complete visual education operating system.

Documentation hierarchy:
README.md
→ docs/ai_context.md
→ docs/vision.md
→ docs/architecture.md
→ docs/roadmap.md

## LearnWithNura Presentation Engine

LearnWithNura is a modular Python presentation automation framework built on `python-pptx`.
It converts structured `slides.txt` content into polished PowerPoint decks using plugin-based layouts, themes, and reusable visual components.

## Project Overview

The engine aims to make slide generation:
- easy to author from plain text,
- extensible through layout plugins,
- maintainable with reusable components,
- backward compatible with legacy content.

## Project Structure

```
learnwithnura-ppt/
├── assets/               # Image and asset files used by decks
├── components/           # Reusable rendering components
├── layouts/              # Layout plugins discovered automatically
├── output/               # Generated PowerPoint files
├── templates/            # Optional slide templates and resources
├── themes/               # Theme definitions for colors and fonts
├── tests/                # Unit tests for framework functionality
├── assets_manager.py     # Asset filesystem helpers
├── config.py             # Project paths and constants
├── generate.py           # Main orchestration entry point
├── icon_manager.py       # Icon selection and helper functions
├── image_manager.py      # Topic image selection
├── parser.py             # Structured content parser and legacy compatibility
├── slides.txt            # Example slide content input
├── utils.py              # Shared drawing helpers and parsers
└── README.md             # Project documentation
```

## Architecture Overview

- `parser.py` reads `slides.txt` and creates `SlideContent` objects.
- `generate.py` orchestrates slide creation and layout selection.
- `layouts/` contains plugin layout classes with auto-discovery.
- `components/` contains reusable rendering primitives.
- `themes/` controls colors, fonts, and visual styling.
- `utils.py` provides shared helper functions for slide rendering.

## Data Flow

```
slides.txt
     │
     ▼
parser.py
     │
     ▼
SlideContent
     │
     ▼
generate.py
     │
     ▼
Layout Registry
     │
     ▼
Layout Plugin
     │
     ▼
Reusable Components
     │
     ▼
python-pptx
     │
     ▼
PowerPoint Output
```

## Adding a New Layout

1. Create a new file in `layouts/`.
2. Subclass `BaseLayout`.
3. Set a unique `name` attribute.
4. Implement `render(self, slide, title, body, context)`.
5. The registry will auto-discover the layout.

## Adding a New Component

1. Create a class in `components/`.
2. Provide a `render()` method with a clean interface.
3. Reuse shared helpers from `utils.py` where possible.
4. Use the component inside layout plugins for composition.

## Running the Project

Install the dependency:

```bash
pip install python-pptx
```

Recommended project workflow:

```bash
python build.py
```

Other supported commands:

```bash
python build.py --health
python build.py --validate
python build.py --generate
python build.py --list-templates
python build.py --preview-template generic_template
python build.py --create-project generic_template --topic "Artificial Intelligence"
```

Generate a deck directly with the existing engine:

```bash
python generate.py
```

Run a lightweight project health check:

```bash
python generate.py --health
```

## Quick Start

1. Choose a template with `python build.py --list-templates`.
2. Load a template with `python build.py --use-template <template_name>`.
3. Edit `slides.txt` as needed.
4. Add a topic image in `assets/` if desired.
5. Run `python build.py`.
6. Open the generated PowerPoint from `output/`.

## Daily Workflow

Normal users only edit:

- `config.py`
- `slides.txt`
- optional topic images in `assets/`

All other files belong to the presentation engine and normally should not be edited.

## Template Workflow

- List available templates:

```bash
python build.py --list-templates
```

- Preview a template with placeholders:

```bash
python build.py --preview-template generic_template --topic "Artificial Intelligence"
```

- Create a content project from a template:

```bash
python build.py --create-project generic_template --topic "Artificial Intelligence"
```

- When a template is loaded into `slides.txt`, the existing `slides.txt` is backed up automatically to `backups/`.
- Backups are named like `slides_YYYYMMDD_HHMMSS.txt` and preserve previous content.

## Content Creation Workflow

1. List templates with `python build.py --list-templates`.
2. Preview a template with `python build.py --preview-template <template> --topic "Your Topic"`.
3. Create the project content with `python build.py --create-project <template> --topic "Your Topic"`.
4. Edit `slides.txt` if desired.
5. Run `python build.py` to generate the PowerPoint.
6. Open the generated file from `output/`.

## Running Tests

```bash
python -m unittest discover tests
```

## Documentation Structure
The repository now contains dedicated documentation folders and prompt templates to support future development.

### New documentation directories
- `docs/` — Core project vision, architecture, roadmap, rules, pedagogy, and glossary.
- `prompts/` — AI prompt templates for master instructions, architecture planning, feature work, and debugging.
- `blueprints/` — Blueprint artifacts and structured plans.

### Key files
- `docs/ai_context.md` — Primary AI onboarding document.
- `docs/architecture.md` — Technical architecture source of truth.
- `docs/roadmap.md` — Transformation roadmap.
- `docs/vision.md` — Long-term product vision.
- `docs/development_rules.md` — Engineering rules and conventions.
- `docs/educational_philosophy.md` — Educational principles.
- `docs/glossary.md` — Central terminology dictionary.
- `prompts/master_prompt.md` — Master AI coding instructions.
- `prompts/architecture_prompt.md` — Architecture planning template.
- `prompts/feature_prompt.md` — Feature implementation template.
- `prompts/debugging_prompt.md` — Debugging workflow template.
- `blueprints/visual_educator_blueprint.md` — Placeholder blueprint artifact.

## How to Use This Documentation
1. Start with `docs/ai_context.md` for AI onboarding.
2. Read `docs/vision.md` to understand long-term product intent.
3. Consult `docs/architecture.md` for system design guidance.
4. Use `docs/roadmap.md` to track phased progress.
5. Follow `docs/development_rules.md` when implementing and reviewing code.
6. Use `prompts/` templates for structured AI planning and execution.

## Maintenance Guidance
- Keep documentation files updated as the platform evolves.
- Add new terms to `docs/glossary.md` when introducing new concepts.
- Align prompt templates with the current AI workflow and development rules.
- Use `docs/roadmap.md` to document completed phases and reprioritize future work.

## Intended Audience
- Human developers working on LearnWithNura.
- AI coding agents onboarding into the repository.
- Product and education leads defining future capabilities.

## Relationships and Navigation
- `docs/ai_context.md` is the starting point for AI agents.
- `docs/vision.md` informs roadmap and architecture decisions.
- `docs/architecture.md` provides technical direction for feature design.
- `docs/roadmap.md` translates vision into phased milestones.
- `docs/development_rules.md` governs engineering behavior.
- `docs/educational_philosophy.md` grounds content strategy and pedagogy.
- `docs/glossary.md` ensures consistent terminology.

