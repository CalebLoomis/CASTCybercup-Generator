class Module_Behavior:

    mod_name = None
    mod_desc = None
    csv_dict_list = None
    passed_dict_list = None

    def __init__(self, module_desc = None, dict_list = None, config_csv = None):
        if module_desc is not None:
            self.mod_desc = module_desc

        if dict_list is not None:
            self.csv_dict_list = csv_list

        if config_csv is not None:
            self.passed_dict_list = dict_list

        #print ("Did I make it?")

    def start(self):
        pass

    def load(self):
        print ("Loaded Module " + self.mod_name)

    def set_desc(self, desc):
        self.mod_desc = desc

    def set_name(self, name):
        self.mod_name = name

    def set_csv_list(self,csv_list):
        self.csv_dict_list = csv_list

    def set_passed_list(self, passed_list):
        self.passed_dict_list = passed_list
