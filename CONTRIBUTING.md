# Contributing

Reality Kernel is in an early seed phase. Contributions should prioritize correctness, reproducibility, and clear provenance.

## Good First Contributions

- Add a Physics Truth Suite experiment with a clear ground-truth law.
- Improve units, tolerances, or citations for an existing experiment.
- Add a small executable benchmark test.
- Improve architecture documentation.

## Benchmark Requirements

Every benchmark should include:

- A stable ID.
- Category.
- Physical law or empirical baseline.
- Inputs and units.
- Expected output and tolerance.
- Source citation.
- Reproducible validation code.

## Engineering Rules

- Keep patches narrow.
- Add or update tests for behavior changes.
- Prefer deterministic benchmarks that can run in CI.
- Do not merge solver changes without benchmark evidence.
- Separate model-generated proposals from validated results.

## License

By contributing, you agree that your contribution will be licensed under the MIT License.
