import unittest
from nlp_dashboard import dashboard

class TestDashboard(unittest.TestCase):

    def test_Dashboard_init(self):
        dash = dashboard.Dashboard()
        self.assertIsNone(dash.stdscr)
        self.assertEqual(dash.panels, {})
        self.assertEqual(dash.tokens, [])

    def test_Panel_init(self):
        panel = dashboard.Panel('test')
        self.assertEqual(panel.name, 'test')
        self.assertEqual(panel.height, 10)
        self.assertEqual(panel.width, 40)

    def test_Dashboard_render(self):
        dash = dashboard.Dashboard()
        dash.stdscr = object()  # Mock the stdscr attribute
        dash.tokens.append((1, 2))
        dash.panels['test'] = object()  # Mock a panel object
        with unittest.mock.patch.object(dash.stdscr, 'addstr') as mock_addstr:
            dash.render()
            self.assertEqual(mock_addstr.call_count, 1)

    def test_Dashboard_display_tokens(self):
        dash = dashboard.Dashboard()
        dash.tokens.append((1, 2))
        with unittest.mock.patch.object(dash.stdscr, 'addstr') as mock_addstr:
            dash.display_tokens()
            self.assertEqual(mock_addstr.call_count, 1)


if __name__ == '__main__':
    unittest.main()
