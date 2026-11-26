**100-point framework: Correctness 40, Edge Cases 30, Quality 20, Security 10. Validated: Strong 92/100 vs Weak 35/100**

# AI Code Evaluator - Prototype RL Environment / Benchmark for Coding Agents

## What it does
Runs lightweight static checks against a Python code file and scores it from 0–100 using `rubric.json`.

## How to Run
```bash
python evaluator.py examples/good_example.py
```

## Rubric

| Category | Weight |
|---|---:|
| Correctness | 40 |
| Edge Cases | 30 |
| Code Quality | 20 |
| Security | 10 |

## Example Failure Analysis
The bad example fails on empty input and has no validation, so it scores **35/100**. The good example scores **92/100** in the benchmark example.

## How this is used as Benchmark
**Task → Agent Code → Evaluator → Score**. Each task supplies a coding problem, an agent submits code, and this evaluator provides a repeatable signal for an RL environment or coding-agent benchmark.
