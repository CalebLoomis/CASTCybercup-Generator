import os, importlib
class modulehandler:

    module_directory = None
    module_list = list()

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
            dir_list = self.list_python_files_in_dir(mod_dir = mod_dir)
            for current in dir_list:

                try:
                    current_module = importlib.import_module(mod_dir + '.' + current)
                except ImportError:
                    print ("cannot import " + current)

                try:
                    loader = getattr(current_module, current)
                    current_obj = loader()
                    self.module_list.append(current_obj)

                    current_obj.load()

                except Exception as e:
                    print ("I can import " + current + ", but I cannot load because:")
                    print (e.args[0] + "\n")

                #print (current)

    def list_python_files_in_dir(self, mod_dir = None):

        ignore_words= "__init__.py Module_Behavior.py"

        output_list = list()
        if mod_dir is None:
            mod_dir = self.module_directory

        try:
            for i in os.listdir(mod_dir):
                if (i[-3::] == ".py" and not i in ignore_words):
                    output_list.append(i[:-3])
        except TypeError:
            print ("Cannot access " + mod_dir + ". Are you sure that one is set?")

        return output_list
