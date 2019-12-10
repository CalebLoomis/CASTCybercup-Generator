"""import os, importlib


dir_path = os.path.dirname(os.path.realpath(__file__))
__all__ = list()
dir = os.listdir(dir_path)
output_list = list()

try:
    for current in dir:
        if (current[-3::] == ".py" and not current == "__init__.py"):
            __all__.append(current[:-3])
except TypeError:
    print ("Cannot access directory")

print (__all__)

__all__.append("load_all")

def load_all(all_modules):
    print ("cool")
"""
