"""
Text Tokenization Module.

This module provides a simple text tokenization function using the standard library's `re` and `string` modules.
"""

import re
import string

def tokenize_text(text: str) -> list[str]:
    """
    Tokenize the given text into individual words or tokens.

    Args:
        text (str): The input text to be tokenized.

    Returns:
        list[str]: A list of tokens extracted from the input text.
    """
    # Remove punctuation
    text_no_punct = re.sub('['+string.punctuation+']', '', text)
    
    # Split into words
    tokens = re.findall(r'\b\w+\b', text_no_punct)
    
    return tokens

def tokenize_text_with_stopwords(text: str, stopwords: list[str]) -> list[str]:
    """
    Tokenize the given text into individual words or tokens and remove stopwords.

    Args:
        text (str): The input text to be tokenized.
        stopwords (list[str]): A list of stopwords to be removed from the tokens.

    Returns:
        list[str]: A list of tokens extracted from the input text with stopwords removed.
    """
    # Tokenize the text
    tokens = tokenize_text(text)
    
    # Remove stopwords
    filtered_tokens = [token for token in tokens if token.lower() not in stopwords]
    
    return filtered_tokens

def main():
    pass  # This module is self-contained and doesn't require a main function.

if __name__ == "__main__":
    main()
