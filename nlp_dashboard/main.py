"""
Entry point and application setup for NLP TUI Dashboard.

This module sets up the dashboard and its components. It is responsible for
initializing the curses library, setting up the UI layout, and starting the
event loop.
"""

import sys
from nlp_dashboard.dashboard import Dashboard
from nlp_dashboard.panel.tokenizer import TokenizerPanel

def main():
    """
    Entry point of the application.

    This function initializes the dashboard and starts the event loop.
    """
    # Initialize curses library
    try:
        import curses
    except ImportError as e:
        print(f"Error: {e}. Please install the 'curses' module.")
        sys.exit(1)

    # Create a new dashboard instance
    dash = Dashboard()

    # Add tokenization panel to the dashboard
    dash.add_panel(TokenizerPanel())

    # Start the event loop
    dash.start()

if __name__ == "__main__":
    main()
