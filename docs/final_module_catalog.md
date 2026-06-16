# Final Module Catalog

## Purpose
This catalog defines the final consolidated module set for LearnWithNura Visual Education OS.
Each module is implementation-ready and scoped to the educational core.

---

## Module: Concept Decomposer

### Purpose
Extract the atomic learning unit from a raw technical idea and make its prerequisites explicit.

### Responsibilities
- Convert raw concept descriptions into a defined learning concept
- Identify hidden prerequisites and dependencies
- Normalize concept scope for pipeline processing
- Split compound concepts into atomic sub-concepts when necessary

### Inputs
- raw concept statement
- technical description or source text
- learner profile/context
- domain tags

### Outputs
- decomposed concept definition
- prerequisite list
- key concept boundaries
- recommended analogy categories
- complexity hints

### Dependencies
- existing parser or text processing utilities
- domain thesaurus or glossary

### Public Interface
- `decompose(rawConcept, context) -> ConceptDefinition`

### Future Expansion Notes
- can later feed into a concept graph or learning path manager
- can be extended to support progressive curriculum sequencing

---

## Module: Simplification Engine

### Purpose
Produce a child-friendly, jargon-minimal explanation for a single learning concept.

### Responsibilities
- Transform decomposed concept text into plain language
- Apply atomic concept and 10-year-old rules
- Eliminate or define technical terms
- Generate glossary entries for remaining terms
- Provide complexity metadata

### Inputs
- decomposed concept definition
- prerequisite list
- learner profile/context

### Outputs
- simplified explanation text
- simplified glossary entries
- complexity score candidate
- simplification metadata

### Dependencies
- Concept Decomposer
- glossary or vocabulary mapping resources
- existing text utilities

### Public Interface
- `simplify(conceptDefinition) -> SimplifiedConcept`

### Future Expansion Notes
- can later support multi-language simplification
- can later integrate with a library of domain-specific simplification patterns

---

## Module: Verification Engine

### Purpose
Evaluate simplified content against educational correctness, clarity, and quality standards.

### Responsibilities
- Score content accuracy and fidelity
- Score simplicity and readability
- Validate prerequisite transparency
- Flag ambiguity, hidden assumptions, and misleading wording
- Produce a verification report and pass/fail decision

### Inputs
- simplified concept
- glossary entries
- complexity metadata
- optional concept source reference

### Outputs
- verification report
- EducationalScore breakdown
- pass/fail result
- recommended revision notes

### Dependencies
- Simplification Engine
- existing content validation utilities

### Public Interface
- `verify(simplifiedConcept) -> VerificationReport`

### Future Expansion Notes
- can later incorporate peer review or human-in-the-loop feedback
- can later integrate with tool-assisted proofreading services

---

## Module: Analogy Engine

### Purpose
Create and validate a real-world analogy that makes the simplified concept more memorable.

### Responsibilities
- Select an appropriate analogy domain
- Generate candidate analogies for the concept
- Validate analogies against structural mapping criteria
- Score analogy quality
- Provide analogy justification notes

### Inputs
- verified simplified concept
- context and learner profile
- candidate analogy categories

### Outputs
- finalized analogy text
- analogy type label
- analogy mapping notes
- analogy score

### Dependencies
- Verification Engine
- Simplification Engine

### Public Interface
- `generateAnalogy(verifiedConcept) -> AnalogyPackage`

### Future Expansion Notes
- can later support multiple analogy variants per concept
- can later include reverse-prompt validation tooling

---

## Module: Visual Explanation Engine

### Purpose
Produce a low-fidelity visual explanation for the concept that mirrors the simplified narrative.

### Responsibilities
- Choose the appropriate visual explanation type
- Map concept entities to visual structures
- Define layout and label rules
- Ensure visual clarity and alignment with text

### Inputs
- verified simplified concept
- final analogy package
- concept structure metadata

### Outputs
- visual explanation specification
- visual format label
- layout directives
- visual score candidate

### Dependencies
- Verification Engine
- Analogy Engine
- existing parser/layout utilities

### Public Interface
- `visualize(verifiedConcept, analogyPackage) -> VisualSpec`

### Future Expansion Notes
- can later support diagram export to additional visual formats
- can later support higher-fidelity illustration templates

---

## Module: Hausa Localization Engine

### Purpose
Adapt simplified content and analogy into Hausa with cultural safety and natural readability.

### Responsibilities
- Translate simplified explanation into Hausa
- Localize analogies and examples culturally
- Define terminology handling for technical terms
- Validate language quality and readability

### Inputs
- verified simplified concept
- final analogy package
- visual specification

### Outputs
- Hausa localized concept text
- cultural anchor notes
- terminology notes
- localization score candidate

### Dependencies
- Verification Engine
- Analogy Engine
- existing translation and localization utilities

### Public Interface
- `localizeToHausa(verifiedConcept, analogyPackage) -> LocalizedPackage`

### Future Expansion Notes
- can later support additional language engines
- can later include native speaker validation workflows

---

## Module: Pipeline Orchestrator

### Purpose
Coordinate the end-to-end flow from raw concept ingestion to final package assembly.

### Responsibilities
- Sequence module execution
- Enforce stage contracts and validation
- Handle failure conditions and revision loops
- Produce the final educational package

### Inputs
- raw concept input package
- pipeline metadata
- execution configuration

### Outputs
- assembled educational package
- stage status metadata
- revision instructions when needed

### Dependencies
- Sprint 1 scope: Concept Decomposer, Simplification Engine, Verification Engine
- existing router or workflow utilities

### Public Interface
- `runPipeline(rawConceptPackage) -> FinalPackage`

### Future Expansion Notes
- can later support batching and workflow orchestration for multiple concepts
- can later integrate with scheduling or CI processes

---

## Module: Output Renderer

### Purpose
Render the final verified educational package into repository outputs.

### Responsibilities
- Convert the final package into deliverable formats
- Produce PowerPoint-ready content and linked assets
- Ensure render output preserves simplified text, analogy, visuals, and localization

### Inputs
- final educational package
- rendering configuration
- asset references

### Outputs
- output artifacts ready for publishing
- rendering status and errors

### Dependencies
- Pipeline Orchestrator
- existing PowerPoint generation engine
- theme and layout registry

### Public Interface
- `render(finalPackage) -> RenderResult`

### Future Expansion Notes
- can later support additional output formats such as PDF or slide carousel exports
- can later integrate with dedicated asset packaging systems
