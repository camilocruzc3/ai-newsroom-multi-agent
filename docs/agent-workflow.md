# Agent workflow and review gates

| Stage | Input | Output | Boundary |
| --- | --- | --- | --- |
| Research | Topics, cutoff date, editorial memory | Candidate stories and evidence | No final drafting or sending |
| Editorial | Verified evidence, editorial guidance | Coherent summaries, implications, narration | No independent claims without evidence |
| Production / QA | Structured edition, optional audio | Draft email and validation results | No automatic authorization |
| Human reviewer | Draft, sources, recipients | Approval or request for changes | Only approved edition may advance |
| Delivery | Authorized immutable edition | Delivery attempt and outcome | External side effect |

## Editorial controls

- Separate publication date from the date an event occurred.
- Prefer primary evidence and keep accessible source URLs.
- Reject unsupported factual claims and obvious duplicate stories.
- Label interpretation as interpretation.
- Review misleading headlines, unsourced figures and repetitive sections.
- Make final audience review and approval explicit.

A model may propose an output; a local system should determine whether an action is permitted. This public repository implements only illustrative lifecycle and editorial validation primitives.