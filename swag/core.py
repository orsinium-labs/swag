from itertools import product
from random import choice

from .map import mapping
from .settings import Settings, default_settings


class Swag(object):
    def __init__(self, **kwargs):
        self.settings = Settings(**default_settings)
        for k, v in kwargs.items():
            if k not in default_settings:
                raise KeyError('Unknown setting: {}'.format(k))
        self.settings.update(kwargs)

        self.mapping = mapping

    def _encode_char(self, char):
        # get variants
        variants = self.mapping.get(char.lower(), None)
        if not variants:
            if self.settings.placeholder_missed is not None:
                return self.settings.placeholder_missed
            return char

        # select right case
        if self.settings.ignore_case:
            variants = ''.join(variants)
        elif variants[0] and char.isupper():
            variants = variants[0]
        elif variants[1] and char.islower():
            variants = variants[1]
        elif self.settings.placeholder_case is not None:
            variants = self.settings.placeholder_case
        else:
            variants = ''.join(variants)

        # choose random char
        if len(variants) == 1:
            return variants[0]
        elif self.settings.offset is not None:
            return variants[offset % len(variants)]
        return choice(variants)

    def _decode_char(self, char):
        possible = []
        for letter, variants in self.mapping.items():
            # apply offset
            if self.settings.offset:
                variants = [
                    variants[0][self.settings.offset % len(variants[0])],
                    variants[1][self.settings.offset % len(variants[1])],
                ]
            # lowercase
            if self.settings.ignore_case or char in variants[1]:
                possible.append(letter)
            # uppercase
            elif char in variants[0]:
                possible.append(letter.upper())

        if possible:
            return possible + [char]
        if self.settings.placeholder_not_found is not None:
            return [self.settings.placeholder_not_found]
        return [char]

    def encode(self, text):
        return ''.join(self._encode_char(char) for char in text)

    def _decode(self, text):
        return [self._decode_char(char) for char in text]

    def decode(self, text):
        return [''.join(s) for s in product(*self._decode(text))]


def swaggify(text, **kwargs):
    return Swag(**kwargs).encode(text)


def deswaggify(text, **kwargs):
    return Swag(**kwargs).decode(text)
