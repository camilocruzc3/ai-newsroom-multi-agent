# Technical decisions

## Specialized stages instead of one unconstrained prompt

Research, editorial interpretation and production have different failure modes. Splitting responsibilities improves inspectability but increases orchestration complexity and model/API calls.

## Structured intermediate artifacts

Source evidence, editorial text, HTML production and delivery authorization should be separate artifacts. This helps identify whether a problem began in evidence collection, writing, formatting or distribution.

## Editorial memory

Comparing candidate stories with recent editions discourages duplicate coverage. A similarity check is not proof that two announcements are the same event, so editorial review remains necessary.

## Deterministic validation outside the LLM

Local code can reliably check required fields, URL shape, text-length constraints and state transitions. It cannot independently verify every fact or editorial judgment. Two small independent samples are included in `src/`.

## Explicit approval before delivery

Email is an irreversible external side effect. A human should approve exact content and recipients; subsequent changes should invalidate that approval. The public state-machine sample is deliberately simpler than a production approval system.

## Optional audio

Audio narration improves accessibility but adds generation latency, cost, hosting and retention obligations. The public version does not generate or upload audio.

## Scope of included components

The included Python examples demonstrate editorial checks and edition lifecycle transitions. Other elements of the full workflow are described in the architecture and illustrated in the application gallery.
