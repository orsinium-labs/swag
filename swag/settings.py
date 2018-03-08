
class Settings(dict):
    def __getattr__(self, name):
        return self[name]


default_settings = dict(
    ignore_case=False,
    offset=None,                # permament offset for choosing one variant
    placeholder_case=None,      # placeholder for chars which case not in alphabet
    placeholder_missed=None,    # placeholder for chars which not in alphabet
)
