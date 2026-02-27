# . * + ? ^ $ [] | () \
import re
# Example 1 - .
print(re.findall(r".at", "cat bat hat mat"))  # ['cat', 'bat', 'hat', 'mat']

# Example 2 - *
print(re.findall(r"ca*t", "ct cat caaat"))  # ['ct', 'cat', 'caaat']

# Example 3 - +
print(re.findall(r"ca+t", "ct cat caaat"))  # ['cat', 'caaat']

# Example 4 - ?
print(re.findall(r"colou?r", "color colour colouur"))  # ['color', 'colour']

# Example 5 - ^ and $
print(re.findall(r"^Total", "Total: $45"))  # ['Total']
print(re.findall(r"\d{2}$", "Amount: 45"))  # ['45']