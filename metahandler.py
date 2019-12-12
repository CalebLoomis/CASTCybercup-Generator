import CSV_handler, os

class metahandler:
    main_list = None
    meta_file = None
    file_dict = None
    ref_file = None

    def __init__ (self, dict_list = None, meta = None):
        if meta is not None:
            if (self.validate_meta(meta)):
                self.meta_file = meta
        if dict_list is not None:
            self.main_list = dict_list

    def validate_meta(self, meta):
        return (os.path.isfile(meta) and CSV_handler.verify_csv(meta))

    def set_meta(self, meta):
        if (self.validate_meta()):
            self.meta_file = meta

    def set_dictlist(self, dict_list):
        self.main_list = dict_list


    def read_meta(self, meta = None):
        file_dict = None

        if (meta is None):
            file_dict = CSV_handler.loadCSV(self.meta_file)

        elif (self.validate_meta(meta)):
            file_dict = CSV_handler.loadCSV(meta)

        else:
            print ("Bad meta file.")
            file_dict = self.file_dict

        self.file_dict = file_dict

    def write_output_using_meta(self, meta = None):
        meta_dict = None

        if (meta is None and self.file_dict is None):
            self.read_meta(meta = self.meta_file)
            meta_dict = self.file_dict
        elif (meta is None):
            meta_dict = self.file_dict

        else:
            self.read_meta(meta=meta)
            meta_dict = self.file_dict
        try:
            for item in meta_dict:
                ref_file = item['filename']
                ref_desc = item['description']
                self.lines_to_file(ref_file, item, ref_desc)
        except TypeError:
            print ("Error. Empty Meta File.")

    #Takes Line as a dict and writes itself to the CSV in the
    def lines_to_file(self, file, line, desc):
        if self.check_dict():
            my_dict_list = self.main_list
            for current_dict in my_dict_list:
                #print (current_dict['type'].lower(), desc.lower())
                if (current_dict['type'].lower() == desc.lower()):
                    #print ("appending")
                    CSV_handler.append_to_csv("Engine/" + file, current_dict)


    def return_csv_dirs(self, meta=None):
        output_list = list()

    def check_dict (self):
        completed = True
        issue_items = list()
        my_dict_list = self.main_list

        for current_dict in my_dict_list:
            for current_key in current_dict:
                if (current_dict[current_key] == None or current_dict[current_key] == ""):
                    completed = False
                    issue_items.append(current_key)

        if not completed:
            for item in issue_items:
                print ("Empty item in dict. check " + item)

        return completed
