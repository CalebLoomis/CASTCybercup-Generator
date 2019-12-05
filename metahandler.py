#import CSV_writer

class metahandler:
    main_list = None
    META_FILE = None

    def __init__ (self, dict_list, meta = None):
        if meta is not None:
            if (self.validate_meta(meta))
                META_FILE = meta
        self.main_list = dict_list

    #I'll do this when I get home. I want to push and go home.
    def validate_meta(self, meta):
        return os.path.isfile(meta)
