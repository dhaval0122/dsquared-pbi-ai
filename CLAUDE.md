# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AI-powered assistant that converts natural language prompts into Power BI DAX measures and applies them to live reports. Requires Power BI Desktop to be open and uses OpenAI GPT-4o-mini for generation.

## Setup

```bash
pip install -e .          # installs package + console script
cp .env.example .env      # then add OPENAI_API_KEY
```

## Running

```bash
python -m pbi_ai.main
# or after pip install -e .
pbi-ai
```

No tests are configured. No Makefile or lint configuration exists.

## Architecture

Data flows through four modules in sequence:

1. **`dashboard_generator.py`** — sends user prompt to OpenAI, returns a JSON plan of DAX measures and structure (table hardcoded to `Sales`, column to `Amount`)
2. **`dax_generator.py`** — lower-level helper that generates a single DAX expression from a prompt; used standalone for simple queries
3. **`main.py`** — orchestrates the pipeline: gets user input → calls `generate_dashboard_plan` → calls `create_measure` via `subprocess`/`pbi` CLI → calls `generate_visual_layout` → calls `update_report_json`
4. **`visual_generator.py`** — returns a hardcoded dict of three visual templates (Card, Line Chart, Bar Chart); not AI-generated
5. **`report_updater.py`** — reads the `.pbip` report's `report.json`, appends a new "AI Dashboard" section with visual containers, writes it back

## Key Constraints

- Power BI Desktop must be open during execution; the `pbi` CLI (external dependency) is called via `subprocess` to create measures
- Table name and column name are hardcoded as `"Sales"` and `"Amount"` in system prompts across `dax_generator.py` and `dashboard_generator.py` — change both files if adapting to a different schema
- Visual layout (`visual_generator.py`) is entirely static; user prompt does not influence which visual types are generated
- `requirements.txt` is empty; real dependencies (`openai`, `python-dotenv`) are declared in `pyproject.toml`
