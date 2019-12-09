"""import os


mod_dir = os.path.dirname(__file__)
try:
    for my_file in os.listdir(mod_dir):
        if (my_file[-3::] == ".py" and not(my_file == '__init__.py')):
            __import__(my_file[:-3])
except TypeError:
    print ("Cannot access folder. Are you sure that one is set?")
"""
