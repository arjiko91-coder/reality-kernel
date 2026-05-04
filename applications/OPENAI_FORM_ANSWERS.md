# OpenAI Grant Form Answers

Prepared: 2026-05-05

## Codex Open Source Fund

Official form: https://openai.com/form/codex-open-source-fund/

### Details

- First name: NEEDS USER CONFIRMATION
- Last name: NEEDS USER CONFIRMATION
- Email address: NEEDS USER CONFIRMATION
- LinkedIn URL: OPTIONAL, NEEDS USER INPUT
- GitHub personal: https://github.com/arjiko91-coder

### Is there anything else you would like us to know?

Reality Kernel is not a simple demo. It is a benchmark-driven attempt to make simulation infrastructure self-correcting. The core technical bottleneck is repeated agentic code repair: Codex must read discrepancy reports, inspect the live solver and adapters, write narrow Python patches, run tests, and iterate across a Physics Truth Suite of 50+ ground-truth experiments. API credits would make it possible to run this loop continuously enough to publish meaningful open results rather than a one-off prototype.

### Which open source project are you representing?

Reality Kernel

### Brief description of the project

Reality Kernel is an open-source agentic physics simulation laboratory. Users describe physical objects and experiments in natural language; Creator and Scientist agents instantiate them in Genesis/MuJoCo/OpenUSD-style simulation workflows; a curated Physics Truth Suite validates results against physical laws and reference data; and an Architect Agent uses Codex CLI to patch the simulation kernel when benchmarks fail.

### GitHub repository

https://github.com/arjiko91-coder/reality-kernel

### If there are other people working with you on this project, please list their names here, and what role they will play in the project

Initial solo-maintainer project. The repository is structured to accept future contributors across physics benchmarks, simulation adapters, agent orchestration, and documentation.

### How would you use API credits for your project?

I would use OpenAI API credits to power the Architect Agent, the self-evolution loop at the center of Reality Kernel. The loop runs the Physics Truth Suite, detects deviations between simulation results and ground-truth baselines, creates discrepancy reports, and invokes Codex CLI to inspect the codebase and write targeted patches to the solver, material model, or simulation adapter.

Each candidate patch is then executed in a sandbox and validated against the full benchmark suite. Passing fixes become pull requests or commits; failing fixes are rejected with structured feedback for another Codex iteration. This is not a single prompt or chat workflow. It requires repeated long-context codebase analysis, patch generation, test execution, and repair across many benchmark cases.

Credits would be used for:

1. Building the first executable benchmark runner for the 50+ experiment Physics Truth Suite.
2. Implementing Genesis, MuJoCo, and OpenUSD integration adapters.
3. Running Codex-driven repair loops against failing mechanics, thermodynamics, fluid dynamics, chemistry, and robotics-contact benchmarks.
4. Producing public evaluation reports that show when Codex-generated patches improve or regress simulation accuracy.
5. Keeping the project fully open source so robotics, physical AI, education, and engineering communities can reuse the benchmark and agentic repair workflow.

Without API credits, the continuous benchmark-driven Codex loop is cost-prohibitive for an independent open-source maintainer. With credits, Reality Kernel can demonstrate a concrete, reproducible example of Codex autonomously improving a real codebase under scientific test constraints.

## Codex For Open Source

Official form: https://openai.com/form/codex-for-oss/

Note: This path is designed primarily for maintainers of important open-source repositories. Reality Kernel is a stronger fit for the Codex Open Source Fund today. It can still be submitted once the public repository exists, but eligibility is less certain until the repo has visible code, issues, stars, downloads, or external usage.

### Name

NEEDS USER CONFIRMATION

### Email

NEEDS USER CONFIRMATION

### GitHub username

arjiko91-coder

### GitHub repository URL

https://github.com/arjiko91-coder/reality-kernel

### Role

Primary maintainer

### Why does this repository qualify? 500 characters max

Reality Kernel targets an open-source gap in physical AI: reproducible benchmark data and repair workflows for validating physics simulation accuracy. The repo will publish a 50+ experiment Physics Truth Suite, Genesis/MuJoCo/OpenUSD adapters, and a Codex-driven maintainer loop that turns benchmark failures into tested code fixes.

### Interested in

- API credits for my project

Codex Security should be requested only after the repository contains enough real code to scan.

### OpenAI organization ID

NEEDS USER CONFIRMATION FROM platform.openai.com

### How do you plan to use API credits for your project? 500 characters max

Use credits to run Codex CLI inside the Architect Agent: parse benchmark failures, inspect solver/adapters, write Python patches, run sandboxed validation across the 50+ experiment Physics Truth Suite, and generate public pull requests or reports. Credits cover repeated repair loops and CI-scale validation.

### Anything else? 500 characters max

I am an independent maintainer with no paid API budget. The project is designed to publish reusable infrastructure: benchmark data, adapters, and an agentic maintenance loop showing how Codex can improve a scientific codebase under tests rather than only answer questions.
