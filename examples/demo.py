"""Demo for Nlp Tui Dashboard."""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import nlp_dashboard

print("Nlp Tui Dashboard", "v" + nlp_dashboard.__version__)
print("modules:", [m for m in dir(nlp_dashboard) if not m.startswith('_')])
