import re

def use_regex(input_text):
    pattern = re.compile(r"[a-zA-Z]+\s[0-9]+\$\.,\(\):", re.IGNORECASE)
    return pattern.match(input_text)


print(use_regex('How To Write A Blog Post + Free Blog Post Template'))