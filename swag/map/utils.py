from .map_en import MAPPING


class Include(object):
    def __init__(self, alphabet):
        self.alphabet = alphabet

    def __call__(self, char, char2=None):
        if char2:
            return self(char), self(char2)

        variants = MAPPING[char.lower()]
        if char.isupper():
            result = variants[0]
        else:
            result = variants[1]
        for c in self.alphabet:
            result = result.replace(c.upper(), '').replace(c.lower(), '')
        return result + char
