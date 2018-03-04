from random import choice


mapping = {
    # source: (UPPER, lower),

    # english
    'a': ('ᐃΔ⋀Λᴧ∧4ÄȺᗩÁ', '@αåá'),
    'b': ('ß8ɃƁ฿', 'ьвƀб6'),
    'c': ('₵ÇȻƇᙅĆ', 'ç¢ȼςć'),
    'd': ('ÐƊḎ', '∂ðđɗ₫Ԁ'),
    'e': ('≣∃3ΣÈɆƐᙓÉЁ', 'êєɇεéɘё'),
    'f': ('Ƒ', 'ϝғ'),
    'g': ('ǤƓǴḠĞ', '9ǥǵ'),
    'h': ('ĦӉӇ', '♄ħн'),
    'i': ('Ì', 'ïιɨí!'),
    'j': ('Ɨ', 'ɉɈ'),
    'k': ('ꝀḰǨ₭', 'ꝁкḱķ'),
    'l': ('ŁĹḺ', 'ℓƖł1ĺ'),
    'm': ('ᙏḾ', '𝔪мϻḿӎɱ'),
    'n': ('ᑎƝŃИṈ', 'ηñπń'),
    'o': ('ÖŐ0ǾØѺΩΘϴ', '⏀∅'),
    'p': ('ⱣƤṔᕈ₱', 'þ⍴'),
    'q': ('ꝖႳϘ', 'ꝗᑫ'),
    'r': ('ЯŘɌᖇŔŘⱤṜ', 'яɍгŕ'),
    's': ('5', 'ѕś'),
    't': ('₸ŦƬ₮', '†т7ŧτ‡'),
    'u': ('ÚỮᙀƱŰṴ⋃', '∪υᵾƲú⊔'),
    'v': ('∀ṾѶ', 'ν▼𝓥'),
    'w': ('⋈ƜШẂ', 'ωᙎшẃώ'),
    'x': ('Ｘ', '✖χ×'),
    'y': ('¥ɎƳӲУ', 'ɏӳɣ'),
    'z': ('ƵŹ', 'ƶźẕ'),
}


RUSSIAN = 'абвгдеёжзийклмнопрстуфхцчшщьъыэюя'

def parent(char, char2=None):
    if char2:
        return parent(char), parent(char2)

    variants = mapping[char.lower()]
    if char.isupper():
        result = variants[0]
    else:
        result = variants[1]
    for c in RUSSIAN:
        result = result.replace(c.upper(), '').replace(c.lower(), '')
    return result


mapping.update({
    # russian
    'а': parent('A', 'a'),
    'б': ('', parent('b')),
    'в': (parent('B'), ''),
    'г': ('', parent('r')),
    'д': parent('D', 'g'),
    'е': parent('E', 'e'),
    'ё': parent('E', 'e'),
    'ж': ('', ''),
    'з': ('3', ''),
    'и': ('ƝÚᙀƱN', '∪υᵾƲ⊔'),
    'й': ('ŃỮŰ', 'ú'),
    'к': parent('K', 'k'),
    'л': ('', ''),
    'м': parent('M', 'm'),
    'н': (parent('H'), ''),
    'о': parent('O', 'o'),
    'п': ('ᑎ', parent('n')),
    'р': parent('P', 'p'),
    'с': parent('C', 'c'),
    'т': parent('T', 't'),
    'у': parent('Y', 'y'),
    'ф': ('Ψ', 'φ'),
    'х': parent('X', 'x'),
    'ц': ('', ''),
    'ч': ('4', ''),
    'ш': parent('W', 'w'),
    'щ': ('', ''),
    'ь': ('', 'ƀb'),
    'ъ': ('', 'ƀ'),
    'ы': ('', ''),
    'э': ('∃Ͽ', ''),
    'ю': ('', ''),
    'я': (parent('R'), ''),
})


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
