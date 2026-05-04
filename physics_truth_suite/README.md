# Physics Truth Suite

Physics Truth Suite is a seed benchmark for validating simulation engines against real physical laws and experimental baselines.

The suite is intended to become an executable benchmark used by Reality Kernel's Architect Agent. Each experiment should eventually include:

- A physical law or empirical reference.
- Input parameters and units.
- Expected output range or tolerance.
- Source citation.
- Simulation setup requirements.
- Pass/fail evaluation code.

The current file, `experiments.yaml`, lists 50+ benchmark candidates across mechanics, thermodynamics, fluid dynamics, electromagnetism, optics, chemistry, materials, and robotics contact dynamics.

## Benchmark Principles

- Prefer simple experiments with clear analytical or trusted empirical baselines.
- Use explicit units and tolerances.
- Separate measurement error from simulation error.
- Track provenance for every constant, law, or dataset.
- Keep each experiment reproducible and small enough for CI.

## Planned Milestones

1. Convert the 50 experiment candidates into a formal JSON schema.
2. Implement five mechanics experiments as executable Python tests.
3. Add reference-data loaders for NIST Chemistry WebBook, PubChem, and Materials Project where allowed by their terms.
4. Add CI that blocks solver changes if benchmark regressions exceed tolerance.
5. Publish contributor guidelines for adding new experiments.
