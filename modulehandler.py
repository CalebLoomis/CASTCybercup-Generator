import os, importlib
class modulehandler:

    module_directory = None
    csv_dir = None
    module_list = list()
    imports_list = list()

    def __init__(self, input_items = None):
        if input_items is not None:

            if "\a" in input_items:
                input_items = input_items.split("\a")
                #print (input_items)
                self.module_directory = input_items[1]
                self.csv_dir = input_items[0]

    def set_new_items(self, input_items):
        if input_items is not None:

            if "\a" in input_items:
                input_items = input_items.split("\a")
                #print (input_items)
                self.module_directory = input_items[1]
                self.csv_dir = input_items[0]

    def load_module(self):

        mod_dir = None
        mod_csv = None
        if self.csv_dir is None or self.module_directory is None:
            print ("Missing mod_dir. Unable to continue.")
        else:
            mod_dir = self.module_directory
            mod_csv = self.csv_dir

        if mod_dir is not None:
            mod_dir = mod_dir[:-3] # Strip out .py
            mod_dir_in_list = mod_dir.split("/")
            import_string = ""
            module_name = mod_dir_in_list[len(mod_dir_in_list) - 1]

            for i in mod_dir_in_list:
                import_string += i + "."

            import_string = import_string [:-1]

            try:
                current_module = importlib.import_module(import_string)

                try:
                    loader = getattr(current_module, module_name)
                    current_obj = loader()
                    #self.module_list.append(current_obj)

                    current_obj.start()
                    #current_obj.load()
                    current_imports = current_obj.get_imports()

                    current_obj.set_csv_file(mod_csv)
                    #print (current_imports)

                    for i in current_imports:
                        self.imports_list.append(i)

                    current_obj.run_each_line()

                except Exception as e:
                    print ("I can import " + module_name + ", but I cannot load because:")
                    print (e.args[0] + "\n")

            except ImportError:
                #try:
                    current_module = importlib.import_module(import_string, package=module_name)

                    try:
                        loader = getattr(current_module, module_name)
                        current_obj = loader()
                        #self.module_list.append(current_obj)

                        current_obj.start()
                        current_obj.load()

                    except Exception as e:
                        print ("I can import " + module_name + ", but I cannot load because:")
                        print (e.args[0] + "\n")
                #except ImportError:
                #    print ("cannot import " + import_string)



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

    def write_modules_output(self, filename="redhatscoring.py"):
        imports = self.imports_list
        print (imports)
        import_line = "import "

        for item in imports:
            import_line += item + ", "

        import_line = import_line[:-2]

        with open (filename, 'w+') as engine_file:
            engine_file.write(import_line)
