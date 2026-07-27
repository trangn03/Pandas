# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A personal pandas learning project built around the Titanic dataset. There is no package, build system, test suite, or linter — it's a sandbox for working through pandas exercises, not production code.

## Structure

- `data/titanic.csv` — the Titanic dataset used for every exercise.
- `note/pandas_learning_guide.md` — a step-by-step pandas tutorial (loading/inspecting, selecting, filtering, cleaning, grouping, transforming). Each step has exercises followed by a `<details>`-collapsed solutions block. The final section is a "Final Challenge" combining all steps.
- `code/titanic.py` — scratch script where the exercises from the guide get worked out in actual runnable code.

## Working in this repo

- Scripts assume the working directory is the repo root, since they load data via the relative path `data/titanic.csv`. Run scripts from the repo root (e.g. `python code/titanic.py`), not from inside `code/`.
- When asked to work through an exercise from `note/pandas_learning_guide.md`, write the attempt into `code/titanic.py` (or a new script in `code/`) rather than pulling from the guide's solutions block — the solutions are answer keys, not code to copy forward.
- Note: the guide's own example code loads the CSV as `pd.read_csv('titanic.csv')` (guide assumes CSV alongside the script), while `code/titanic.py` uses `pd.read_csv('data/titanic.csv')` (actual repo layout). Follow the path used in `code/titanic.py` when writing runnable scripts.
