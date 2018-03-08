from .utils import Include


include = Include('абвгдеёжзийклмнопрстуфхцчшщьъыэюя')

MAPPING = {
    # russian
    'а': include('A', 'a'),
    'б': ('', include('b')),
    'в': (include('B'), ''),
    'г': ('', include('r')),
    'д': include('D', 'g'),
    'е': include('E', 'e'),
    'ё': include('E', 'e'),
    'ж': ('', ''),
    'з': ('3', ''),
    'и': ('ƝÚᙀƱN', '∪υᵾƲ⊔'),
    'й': ('ŃỮŰ', 'ú'),
    'к': include('K', 'k'),
    'л': ('', ''),
    'м': include('M', 'm'),
    'н': (include('H'), ''),
    'о': include('O', 'o'),
    'п': ('ᑎ', include('n')),
    'р': include('P', 'p'),
    'с': include('C', 'c'),
    'т': include('T', 't'),
    'у': include('Y', 'y'),
    'ф': ('Ψ', 'φ'),
    'х': include('X', 'x'),
    'ц': ('', ''),
    'ч': ('4', ''),
    'ш': include('W', 'w'),
    'щ': ('', ''),
    'ь': ('', 'ƀb'),
    'ъ': ('', 'ƀ'),
    'ы': ('', ''),
    'э': ('∃Ͽ', ''),
    'ю': ('', ''),
    'я': (include('R'), ''),
}
