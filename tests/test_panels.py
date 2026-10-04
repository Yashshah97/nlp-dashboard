import unittest
from nlp_dashboard import panels

class TestPanels(unittest.TestCase):
    def test_token_distribution_panel_render(self):
        panel = panels.TokenDistributionPanel("Token Distribution")
        data = {'token_counts': {'hello': 5, 'world': 3}}
        self.assertEqual(panel.render(data), "Token Distribution\nhello: 5\nworld: 3")

    def test_token_frequency_panel_render(self):
        panel = panels.TokenFrequencyPanel("Token Frequency")
        data = {'token_freqs': {'hello': 0.2, 'world': 0.1}}
        self.assertEqual(panel.render(data), "Token Frequency\nhello: 20.00%\nworld: 10.00%")

    def test_sentiment_analysis_panel_render(self):
        panel = panels.SentimentAnalysisPanel("Sentiment Analysis")
        data = {'sentiment': 0.5}
        self.assertEqual(panel.render(data), "Sentiment Analysis\nSentiment: 50.00")

if __name__ == '__main__':
    unittest.main()
