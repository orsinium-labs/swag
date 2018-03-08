from .map_en import MAPPING as map_en
from .map_ru import MAPPING as map_ru

mapping = map_en.copy()
mapping.update(map_ru)
