# Verification System Design

## Purpose
This document designs the LearnWithNura verification subsystem. It defines scoring, pass/fail logic, thresholds, revision workflow, and report format for educational quality assurance.

---

## Verification Architecture
The verification system is a centralized evaluation engine that receives simplified educational content and returns a structured report with scores across five dimensions:
- AccuracyScore
- SimplicityScore
- AnalogyScore
- VisualScore
- LocalizationScore

A final aggregated score is computed and used to determine pass or fail.

---

## Scoring Engine

### Score Dimensions
- `AccuracyScore` (0-100)
- `SimplicityScore` (0-100)
- `AnalogyScore` (0-100)
- `VisualScore` (0-100)
- `LocalizationScore` (0-100)

### Dimension Definitions
- **AccuracyScore**: measures factual correctness and mechanism fidelity.
- **SimplicityScore**: measures readability, jargon elimination, and atomic clarity.
- **AnalogyScore**: measures analogy relevance, fidelity, and non-misleading quality.
- **VisualScore**: measures visual clarity, alignment, and interpretability.
- **LocalizationScore**: measures Hausa translation quality and cultural fit.

### Weighting Engine
The weights are designed to prioritize correctness and simplicity while still valuing analogy, visualization, and localization.
- `AccuracyWeight`: 0.30
- `SimplicityWeight`: 0.25
- `AnalogyWeight`: 0.15
- `VisualWeight`: 0.15
- `LocalizationWeight`: 0.15

### FinalScore Calculation
`FinalScore = (AccuracyScore * 0.30) + (SimplicityScore * 0.25) + (AnalogyScore * 0.15) + (VisualScore * 0.15) + (LocalizationScore * 0.15)`

---

## Threshold System

### Individual Thresholds
- `AccuracyScore >= 80`
- `SimplicityScore >= 80`
- `AnalogyScore >= 70`
- `VisualScore >= 70`
- `LocalizationScore >= 70`

### Final Pass Thresholds
- `FinalScore >= 80`
- All individual thresholds met
- No critical issues present

### Pass Status
- `passStatus = true` only when all thresholds are satisfied and no critical issue remains.
- `passStatus = false` when any threshold is unmet or critical issues exist.

---

## Revision Workflow

### Step 1: Initial Verification
- Input: simplified concept package
- Output: verification report
- If pass: forward to analogy stage
- If fail: return revision instructions to simplification stage

### Step 2: Revision Cycle
- Input: revised simplified concept
- Re-run verification
- Keep track of iteration count
- If iterations > 3 and still failing, escalate for design review

### Step 3: Final Verification Gate
- Input: assembled package after all stages
- Output: final verification report
- If pass: mark ready for output
- If fail: identify the earliest failing stage and return package for revision

### Iteration Rules
- Allow up to 3 revision cycles per package before requiring manual review.
- Each revision must address concrete issues from the verification report.
- Revision reports must include the before/after change summary.

---

## Report Format

### VerificationReport
- `conceptId`: string
- `accuracyScore`: integer
- `simplicityScore`: integer
- `analogyScore`: integer
- `visualScore`: integer
- `localizationScore`: integer
- `finalScore`: integer
- `passStatus`: boolean
- `issues`: array[object]
  - `issueId`: string
  - `category`: string
  - `severity`: string
  - `description`: string
  - `recommendation`: string
- `recommendationLevel`: string
- `revisionCount`: integer
- `generatedAt`: string

### Issue Severity Levels
- `critical`: blocks pass
- `major`: needs revision before final output
- `minor`: can be improved later, but not blocking

### Recommendation Levels
- `ready`: no further work needed
- `revise`: changes required
- `redesign`: core concept or structure is invalid

---

## Score Definitions

### EducationalScore
Aggregated view of the report, not a separate numeric value. It is the combination of all five scores and is captured by `finalScore`.

### AccuracyScore
Factors:
- factual correctness
- fidelity to conceptual mechanisms
- avoidance of misleading simplifications

### SimplicityScore
Factors:
- plain language
- sentence length
- atomicity
- glossary coverage

### AnalogyScore
Factors:
- familiarity
- structural fidelity
- clarity
- non-misleading quality

### VisualScore
Factors:
- structure clarity
- entity mapping
- label accuracy
- whitespace and hierarchy

### LocalizationScore
Factors:
- accuracy of Hausa meaning
- cultural relevance
- terminology handling
- natural flow

---

## Pseudocode

### Score aggregation pseudocode
```
function computeScores(input):
    accuracy = evaluateAccuracy(input)
    simplicity = evaluateSimplicity(input)
    analogy = evaluateAnalogy(input)
    visual = evaluateVisual(input)
    localization = evaluateLocalization(input)

    final = (accuracy * 0.30) +
            (simplicity * 0.25) +
            (analogy * 0.15) +
            (visual * 0.15) +
            (localization * 0.15)

    pass = all([
        accuracy >= 80,
        simplicity >= 80,
        analogy >= 70,
        visual >= 70,
        localization >= 70,
        final >= 80
    ])

    report = {
        'accuracyScore': accuracy,
        'simplicityScore': simplicity,
        'analogyScore': analogy,
        'visualScore': visual,
        'localizationScore': localization,
        'finalScore': final,
        'passStatus': pass,
        'issues': collectIssues(input),
        'recommendationLevel': determineRecommendation(pass),
    }
    return report
```

### Revision workflow pseudocode
```
function verifyPackage(package):
    report = computeScores(package)
    if report.passStatus:
        return report

    package.revisionCount += 1
    if package.revisionCount > 3:
        report.recommendationLevel = 'redesign'
        return report

    revise(package, report.issues)
    return verifyPackage(package)
```

### Final gate pseudocode
```
function finalGate(finalPackage):
    report = computeScores(finalPackage)
    if not report.passStatus:
        report.issues.append({
            'issueId': 'final_gate',
            'category': 'package',
            'severity': 'critical',
            'description': 'Final verification gate failed.',
            'recommendation': 'Revise the stage outputs according to issue list.'
        })
    return report
```

---

## Implementation Notes
- The verification system is intentionally rule-based and deterministic.
- It should operate after simplification and again after package assembly.
- All failure explanations must be actionable and tied to specific content dimensions.
- The engine should be designed to allow later integration with human review.
