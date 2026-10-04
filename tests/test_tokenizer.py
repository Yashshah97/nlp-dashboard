import unittest
from nlp_dashboard import tokenizer

class TestTokenizer(unittest.TestCase):

    def test_tokenize_text(self):
        text = "Hello, World!"
        tokens = tokenizer.tokenize_text(text)
        self.assertEqual(tokens, ["Hello", "World"])

    def test_tokenize_text_with_stopwords(self):
        text = "hello world"
        stopwords = ["hello"]
        tokens = tokenizer.tokenize_text_with_stopwords(text, stopwords)
        self.assertEqual(tokens, ["world"])

if __name__ == "__main__":
    unittest.main()
