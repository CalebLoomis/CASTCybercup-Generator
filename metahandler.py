import CSV_handler

class metahandler:
    main_list = None
    meta_file = None

    def __init__ (self, dict_list, meta = None):
        if meta is not None:
            if (self.validate_meta(meta)):
                meta_file = meta
        self.main_list = dict_list

    #I'll do this when I get home. I want to push and go home.
    def validate_meta(self, meta):
        return (os.path.isfile(meta) and CSV_handler.verify_csv(meta))

    def set_meta(self, meta):
        if (self.validate_meta()):
            self.meta_file = meta
