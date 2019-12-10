class Module_Behavior:

    mod_desc = None
    csv_dict_list = None
    passed_dict_list = None

    def __init__(self, module_desc = None, dict_list = None, csv_list = None):
        if module_desc is not None:
            self.mod_desc = module_desc

        if dict_list is not None:
            self.csv_dict_list = csv_list

        if csv_list is not None:
            self.passed_dict_list = dict_list

        #print ("Did I make it?")


    def load(self):
      print ("Loaded Module")
