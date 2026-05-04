# Roadmap

## Phase 0: Grant-Review Seed

- Publish project README, license, architecture notes, and Physics Truth Suite seed.
- Define the benchmark schema.
- Add a minimal executable benchmark runner.
- Prepare OpenAI grant applications.

## Phase 1: Executable Truth Suite

- Implement five mechanics benchmarks:
  - Small-angle pendulum.
  - Projectile motion.
  - Hooke law oscillator.
  - Elastic collision.
  - Inclined plane acceleration.
- Add unit-aware input and output formats.
- Generate structured benchmark reports.

## Phase 2: Simulation Adapters

- Add a generic adapter protocol.
- Implement a first MuJoCo adapter.
- Implement a first Genesis adapter.
- Export simple OpenUSD scene assets.

## Phase 3: Architect Agent Loop

- Convert benchmark failures into discrepancy reports.
- Invoke Codex CLI with bounded repair prompts.
- Run candidate patches in a sandbox.
- Reject patches that regress any benchmark.
- Publish validation reports with each accepted change.

## Phase 4: Scientific Data Integrations

- Add reference-data loaders for allowed public sources.
- Track citation and provenance metadata.
- Expand chemistry and materials experiments.

## Phase 5: Community Release

- Write contributor docs for new benchmarks.
- Add CI templates.
- Publish example notebooks.
- Invite robotics, physical AI, and education contributors.
