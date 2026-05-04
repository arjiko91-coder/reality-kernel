# Reality Kernel

Reality Kernel is an open-source, agentic physics simulation laboratory designed to test physical ideas before they are built in the real world.

The project combines LLM agents, real-time physics engines, scientific data sources, and benchmark-driven self-correction. Its long-term goal is to let a user describe a physical object or experiment in natural language, instantiate it inside a physically meaningful simulation, run structured experiments, compare the results against ground truth, and improve the simulation code when it is wrong.

## Core Idea

Most simulation systems are static tools: humans configure scenes, run tests, inspect errors, and manually patch the engine or model assumptions. Reality Kernel is designed as a self-improving research environment where agents can generate objects, run experiments, identify discrepancies, write corrective patches, and validate those patches against a curated benchmark suite.

## Architecture

Reality Kernel has three tightly integrated AI layers.

### Creator Agent

The Creator Agent accepts natural language requests such as:

```text
Create an aluminum cylinder with radius 5 cm, height 10 cm, density 2700 kg/m^3, and a rough anodized surface.
```

It produces structured scene assets, including:

- OpenUSD-compatible 3D objects.
- Geometry and mass properties.
- Material metadata sourced from scientific references such as PubChem and Materials Project.
- Simulation-ready parameters for downstream physics engines.

### Scientist Agent

The Scientist Agent turns user goals into testable experiments. It can:

- Formulate hypotheses.
- Build simulation scenes.
- Run experiments in Genesis, MuJoCo, or other adapters.
- Log measurements in structured form.
- Compare simulation output to physical laws or curated ground-truth baselines.

### Architect Agent

The Architect Agent is the novel self-evolution loop.

It monitors simulation accuracy against the Physics Truth Suite. When a discrepancy is detected, it creates a structured report, asks Codex CLI to inspect the codebase and write a targeted patch, runs the patch in a sandbox, validates it against the full benchmark suite, and prepares the fix for merge only if the benchmark passes.

The intended loop is:

1. Run benchmark experiments.
2. Detect a deviation from ground truth.
3. Generate a discrepancy report.
4. Use Codex CLI with OpenAI models to inspect the solver and write a patch.
5. Run validation in an isolated environment.
6. Accept the patch only if it improves the failing case without regressing the suite.

## Physics Truth Suite

The Physics Truth Suite is a curated open benchmark of physical experiments for validating simulation accuracy. It starts with 50+ experiments across:

- Mechanics
- Thermodynamics
- Fluid dynamics
- Electromagnetism
- Optics and waves
- Chemistry and materials
- Robotics contact dynamics

See [physics_truth_suite/experiments.yaml](physics_truth_suite/experiments.yaml).

## Why Codex Matters

Reality Kernel depends on agentic coding rather than one-off code generation. The Architect Agent needs to repeatedly read a live codebase, understand failing benchmark reports, write narrow solver patches, run tests, and iterate until the kernel improves.

This is the workflow Codex CLI is designed for: codebase understanding, targeted implementation, validation, and multi-step repair inside a real repository.

## Open Source Plan

The project will release:

- Agent orchestration code.
- Genesis, MuJoCo, and OpenUSD integration adapters.
- The Physics Truth Suite benchmark dataset.
- Reproducible benchmark runners.
- Documentation for adding new ground-truth experiments.

## Current Status

This repository is an early project seed prepared for open-source development and grant review.

Current assets:

- Project architecture.
- Initial README.
- MIT license.
- Physics Truth Suite seed list with 50+ benchmark experiments.

Planned next steps:

1. Implement the benchmark schema and runner.
2. Build a minimal MuJoCo/Genesis adapter.
3. Add the first five executable truth-suite experiments.
4. Implement discrepancy reports.
5. Connect Codex CLI to the Architect Agent patch loop.

## License

MIT License. See [LICENSE](LICENSE).
