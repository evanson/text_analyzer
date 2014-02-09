import re

## Splits text into tokens, matches text-only words and returns a list of these
def tokenize(text):
    words = []
    regex = re.compile("[a-zA-Z']+")
    tokens = text.split()
    for token in tokens:
        m = regex.match(token)
        if hasattr(m, 'group'):
            plain_word = m.group()
            words.append(plain_word.lower())
    return words


