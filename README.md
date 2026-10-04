# Nlp Tui Dashboard

This is a command-line interface (CLI) to explore the inner workings of natural language processing (NLP) techniques through an interactive dashboard. The Nlp Tui Dashboard provides real-time visualization of text tokenization and analysis results, allowing users to gain insights into their data with ease. Built in pure Python, it includes comprehensive tests and documentation for maximum reliability and usability.

## What makes it unique

Combines text tokenization and analysis with a live-updating curses dashboard with panels and sparklines — a niche where few ready-made tools exist.

## Features

- **`nlp_dashboard/dashboard.py`** — TUI dashboard logic
- **`nlp_dashboard/panels.py`** — Panel implementations for tokenization and analysis
- **`nlp_dashboard/sparklines.py`** — Sparkline visualizations for metrics
- **`nlp_dashboard/tokenizer.py`** — Text tokenization module
- **`nlp_dashboard/analysis.py`** — Text analysis module with metrics calculation
- **`nlp_dashboard/main.py`** — Entry point and application setup

## Tech stack

- **Python 3** — pure standard library, **zero external dependencies**
- **unittest** for the test suite (6/6 module suites passing)
- Local-first: no network calls, no API keys, runs anywhere Python runs

## How to run

```bash
git clone https://github.com/Yashshah97/nlp-dashboard.git
cd nlp-dashboard

# run the demo
python3 examples/demo.py

# run the tests
python3 -m unittest discover -s tests -t .
```

No installation step is needed — there is nothing to `pip install`.

## Project structure

```
nlp-dashboard/
├── nlp_dashboard/
│   ├── dashboard.py
│   ├── panels.py
│   ├── sparklines.py
│   ├── tokenizer.py
│   ├── analysis.py
│   ├── main.py
├── tests/               # unittest suite (verified passing)
├── examples/demo.py     # runnable demo (verified)
├── docs/
└── README.md
```

See [docs/PLAN.md](docs/PLAN.md) for the architecture and
[docs/usage.md](docs/usage.md) for API notes.

## About

Domain: **nlp** · Archetype: **dashboard** ·
Built autonomously by JARVIS on 2026-10-04. MIT licensed.
