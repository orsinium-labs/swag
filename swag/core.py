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

    def encode(self, text):
        return ''.join(self._encode_char(char) for char in text)


def swaggify(text, **kwargs):
    return Swag(**kwargs).encode(text)
