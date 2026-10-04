import unittest
from nlp_dashboard import main

class TestMain(unittest.TestCase):

    def test_main_imports(self):
        self.assertIsNotNone(main.main)
        self.assertIsNotNone(main.Dashboard)

    def test_main_curses_import(self):
        try:
            import curses
        except ImportError as e:
            self.fail(f"Expected 'curses' to be installed, but got: {e}")

    def test_main_dashboard_creation(self):
        dash = main.Dashboard()
        self.assertIsNotNone(dash)

if __name__ == "__main__":
    unittest.main()
