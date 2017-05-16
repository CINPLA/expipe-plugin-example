# This imports all plugins when loading expipe.
import my_plugin


def reveal():
    import os.path as op
    print(__file__)
