import CSV_handler, os

class metahandler:
    main_list = None
    meta_file = None
    file_dict = None

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
        self.main_list = main_list

    def read_meta(self, meta = None):
        file_dict = None

        if (meta is None):
            meta = self.meta_file

        if (self.validate_meta(meta)):
            file_dict = CSV_handler.loadCSV(meta)
            for line in file_dict:
                self.line_to_file(line)


        else:
            print ("Bad meta file.")

        self.file_dict = file_dict
        return (self.file_dict)

    #Takes Line as a dict and writes itself to the CSV in the
    def line_to_file(self, line):
        completed = True
        issue_items = list()
        my_dict_list = self.main_list

        for current_dict in my_dict_list:
            for current_key in current_dict:
                if (current_dict[current_key] == None or current_dict[current_key] == ""):
                    completed = False
                    issue_items.append(current_key)

        if completed:
            outfile = line['filename']

        else:
            for item in issue_items:
                print ("Empty item in dict. check " + item)
