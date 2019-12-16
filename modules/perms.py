from Module_Behavior import *

class perms (Module_Behavior):
    mod_name = None

    def start(self, csv_file = None):
        if csv_file is not None:
            pass

        print ("Setting up Perms Module...")
        self.mod_name = "perms"


    def load(self):
        print ("Loaded perms")
