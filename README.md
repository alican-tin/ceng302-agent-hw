# CENG302 Agent Homework Sandbox

This repository is a small Python sandbox used to practice GitHub Copilot agent workflows (research, testing, security scanning, and documentation).

## Project Overview

The project contains four modules created for guided improvement tasks:

- `spaghetti_logic.py`: data processing code originally written in a non-modular style.
- `failing_calculator.py`: ratio-average calculation that originally crashed on zero input.
- `secret_leak.py`: intentionally insecure example containing a hardcoded secret.
- `mystery_module.py`: mathematical utility with unclear naming.

## Module Details

### `mystery_module.py`

`mystery_module.py` defines this function:

- `fn_x(a, b, c)`

The function solves the quadratic equation:

\[ ax^2 + bx + c = 0 \]

It computes the discriminant:

\[ d = b^2 - 4ac \]

Behavior:

- If `d < 0`, it returns `None` (no real roots).
- If `d >= 0`, it returns a tuple with two real roots using the quadratic formula:

\[
\left(\frac{-b + \sqrt{d}}{2a},\; \frac{-b - \sqrt{d}}{2a}\right)
\]

In short, `fn_x` is a quadratic root finder for real-number roots.

## Notes

- This repository is intentionally educational and includes examples of bad practices for training/refactoring purposes.
- Security-sensitive examples (like hardcoded credentials) should never be used in real projects.
