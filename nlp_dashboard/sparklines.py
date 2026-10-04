"""
Sparkline visualizations for metrics.

This module provides a simple way to create sparklines using the `text` module.
"""

import textwrap

def render_sparkline(values):
    """
    Render a sparkline given a list of values.

    Args:
        values (list): A list of values to display in the sparkline.

    Returns:
        str: The rendered sparkline as a string of asterisks (*).
    """
    if not values:
        return ""

    min_value = min(values)
    max_value = max(values)

    scale_factor = 20 / (max_value - min_value) if max_value != min_value else 1
    scaled_values = [int((value - min_value) * scale_factor) for value in values]

    wrapped_lines = []
    line_length = 0

    for i, value in enumerate(scaled_values):
        num_asterisks = int(value / 2)
        if num_asterisks > 0:
            line = "*" * num_asterisks
            line_length += len(line) + 1
            wrapped_lines.append(line)

    return "\n".join(wrapped_lines).lstrip()

def render_sparkline_with_labels(values, labels):
    """
    Render a sparkline with labels given a list of values and corresponding labels.

    Args:
        values (list): A list of values to display in the sparkline.
        labels (list): A list of labels corresponding to each value.

    Returns:
        str: The rendered sparkline as a string of asterisks (*) with labels.
    """
    if not values or not labels:
        return ""

    wrapped_lines = []
    for i, (value, label) in enumerate(zip(values, labels)):
        num_asterisks = int(value / 2)
        line = f"{label}: {'*' * num_asterisks}"
        wrapped_lines.append(line)

    return "\n".join(wrapped_lines).lstrip()

if __name__ == "__main__":
    values = [1, 5, 10, 15, 20]
    print(render_sparkline(values))
    print(render_sparkline_with_labels(values, ["A", "B", "C", "D", "E"]))
