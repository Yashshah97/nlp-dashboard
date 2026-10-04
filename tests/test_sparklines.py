import unittest
from nlp_dashboard import sparklines

class TestSparklines(unittest.TestCase):
    def test_render_sparkline(self):
        values = [1, 5, 10, 15, 20]
        self.assertEqual(render_sparkline(values), "*****\n***\n**\n*\n")

    def test_render_sparkline_with_labels(self):
        values = [1, 5, 10, 15, 20]
        labels = ["A", "B", "C", "D", "E"]
        self.assertEqual(render_sparkline_with_labels(values, labels), 
                         "A: *****\nB: ***\nC: **\nD: *\nE: ")

    def test_render_sparkline_empty_values(self):
        values = []
        self.assertEqual(render_sparkline(values), "")

    def test_render_sparkline_with_single_value(self):
        values = [10]
        self.assertEqual(render_sparkline(values), "**")

if __name__ == "__main__":
    unittest.main()
