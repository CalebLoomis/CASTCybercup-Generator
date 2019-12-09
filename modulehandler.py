import os
class modulehandler:

    module_directory = None

    def __init__(self, mod_dir = None):
        if mod_dir is not None:
            self.module_directory = mod_dir
            self.load_modules (mod_dir=mod_dir)

    def load_modules(self, mod_dir = None):
        if mod_dir is None and self.module_directory is None:
            print ("Missing mod_dir. Unable to continue.")
        elif mod_dir is None:
            mod_dir = self.module_directory

        if mod_dir is not None:
            listed_modules = self.list_python_files_in_dir(mod_dir = mod_dir)
            for module in listed_modules:
                import_string = mod_dir + "." + module
                current = __import__(import_string)
                current.load()

    def list_python_files_in_dir(self, mod_dir = None):

        output_list = list()
        if mod_dir is None:
            mod_dir = self.module_directory

        try:
            for i in os.listdir(mod_dir):
                if (i[-3::] == ".py"):
                    output_list.append(i[:-3])
        except TypeError:
            print ("Cannot access " + mod_dir + ". Are you sure that one is set?")

        return output_list
