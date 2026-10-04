"""
Panel implementations for text tokenization and analysis.

Each panel displays a specific aspect of the input text. The panels are designed to be extensible,
so you can easily add or remove panels as needed.
"""

class TokenDistributionPanel:
    """Displays the distribution of tokens in the input text."""

    def __init__(self, title):
        self.title = title

    def render(self, data):
        """Render the panel with the given data."""
        token_counts = data['token_counts']
        return f"{self.title}\n" + "\n".join(f"{token}: {count}" for token, count in token_counts.items())


class TokenFrequencyPanel:
    """Displays the frequency of each token in the input text."""

    def __init__(self, title):
        self.title = title

    def render(self, data):
        """Render the panel with the given data."""
        token_freqs = data['token_freqs']
        return f"{self.title}\n" + "\n".join(f"{token}: {freq:.2f}%" for token, freq in token_freqs.items())


class SentimentAnalysisPanel:
    """Displays the sentiment analysis results."""

    def __init__(self, title):
        self.title = title

    def render(self, data):
        """Render the panel with the given data."""
        return f"{self.title}\n" + f"Sentiment: {data['sentiment']:.2f}"
