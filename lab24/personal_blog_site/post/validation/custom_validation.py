import re

with open("post/validation/swear_words.txt") as f:
    CENSORED_WORDS = f.read().splitlines()


def validate_comment_content(text):
    words = list(re.sub("[^\w]", " ", text).lower().split())
    return any(censored_word in words for censored_word in CENSORED_WORDS)
