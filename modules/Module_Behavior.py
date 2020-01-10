import CSV_handler

class Module_Behavior(object):

    mod_name = None
    mod_desc = None
    csv_file = None
    passed_dict_list = None
    to_import = list()
    imports = list()
    conditions = list()
    vars = {}

    def __init__(self, module_desc = None, dict_list = None, config_csv = None):
        if module_desc is not None:
            self.mod_desc = module_desc

        if dict_list is not None:
            self.csv_file = csv_list

        if config_csv is not None:
            self.passed_dict_list = dict_list

        #print ("Did I make it?")

    def start(self):
        pass

    def load(self, csv_row):
        print ("Loaded Module " + self.mod_name)

    def set_desc(self, desc):
        self.mod_desc = desc

    def set_name(self, name):
        self.mod_name = name

    def get_conditions(self):
        return self.conditions

    def set_csv_file(self,csv_list):
        self.csv_file = csv_list

    def set_passed_list(self, passed_list):
        self.passed_dict_list = passed_list

    def get_imports(self):
        #can_add = True
        for i in self.imports:
            #print (i)
            if (self.check_import_dupe(i)):
                self.to_import.append(i)

        return (self.to_import)

    def check_import_dupe(self, module):
        can_add = True
        for i in self.to_import:
            if (i == module):
                print (i, module)
                can_add = False

        return can_add

    def add_point(self, conditional, point_text):
        self.conditions.append ({"conditional" : conditional, "point_text" : point_text})

    def run_each_line(self):
        lines = CSV_handler.loadCSV(self.csv_file)
        for line in lines:
            self.load(line)
