from random import choice
from .map import mapping


def swaggify(text, *, ignore_case=False, offset=None, placeholder_case=None, placeholder_missed=None):
    result = []
    for char in text:
        # get variants
        variants = mapping.get(char.lower(), None)
        if not variants:
            if placeholder_missed is None:
                result.append(char)
            else:
                result.append(placeholder_missed)
            continue

        # select right case
        if ignore_case:
            variants = ''.join(variants)
        elif variants[0] and char.isupper():
            variants = variants[0]
        elif variants[1] and char.islower():
            variants = variants[1]
        elif placeholder_case is None:
            variants = ''.join(variants)
        else:
            variants = placeholder_case

        # choice random char
        if len(variants) == 1:
            result.append(variants[0])
        elif offset is None:
            result.append(choice(variants))
        else:
            result.append(variants[offset % len(variants)])

    return ''.join(result)
