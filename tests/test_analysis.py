import unittest
from nlp_dashboard import analysis

class TestAnalysisModule(unittest.TestCase):

    def test_calculate_word_freq(self):
        text = "This is a sample text"
        freq_dict = analysis.calculate_word_freq(text)
        self.assertEqual(len(freq_dict), 4)

    def test_calculate_char_freq(self):
        text = "Hello World!"
        char_freq_dict = analysis.calculate_char_freq(text)
        self.assertIn('H', char_freq_dict)
        self.assertIn('W', char_freq_dict)

    def test_calculate_tokenization_stats(self):
        text = "This is a sample text"
        stats = analysis.calculate_tokenization_stats(text)
        self.assertEqual(stats['num_words'], 4)
        self.assertEqual(stats['num_chars'], 19)

    def test_calculate_sentiment_score(self):
        # This test will fail because the sentiment scoring system
        # is very basic and doesn't handle edge cases.
        text = "This is a great text"
        score = analysis.calculate_sentiment_score(text)
        self.assertGreater(score, 0.5)

if __name__ == '__main__':
    unittest.main()
