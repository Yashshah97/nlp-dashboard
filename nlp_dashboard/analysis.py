"""
Text Analysis Module.

This module provides a set of functions for calculating text analysis metrics.
"""

from typing import Dict, List

def calculate_word_freq(text: str) -> Dict[str, int]:
    """
    Calculate word frequency in the given text.

    Args:
        text (str): The input text.

    Returns:
        Dict[str, int]: A dictionary with words as keys and their frequencies as values.
    """
    words = text.split()
    freq_dict = {}
    for word in words:
        if word not in freq_dict:
            freq_dict[word] = 1
        else:
            freq_dict[word] += 1
    return freq_dict

def calculate_char_freq(text: str) -> Dict[str, int]:
    """
    Calculate character frequency in the given text.

    Args:
        text (str): The input text.

    Returns:
        Dict[str, int]: A dictionary with characters as keys and their frequencies as values.
    """
    char_freq_dict = {}
    for char in text:
        if char not in char_freq_dict:
            char_freq_dict[char] = 1
        else:
            char_freq_dict[char] += 1
    return char_freq_dict

def calculate_tokenization_stats(text: str) -> Dict[str, int]:
    """
    Calculate tokenization statistics for the given text.

    Args:
        text (str): The input text.

    Returns:
        Dict[str, int]: A dictionary with tokenization statistics.
    """
    words = text.split()
    return {
        'num_words': len(words),
        'num_chars': len(text)
    }

def calculate_sentiment_score(text: str) -> float:
    """
    Calculate the sentiment score of the given text.

    Args:
        text (str): The input text.

    Returns:
        float: The sentiment score.
    """
    # For simplicity, we assume a simple sentiment scoring system
    # where positive words are assigned +1 and negative words -1
    positive_words = ['good', 'great']
    negative_words = ['bad', 'terrible']

    score = 0
    for word in text.split():
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1

    return score / len(text.split())
