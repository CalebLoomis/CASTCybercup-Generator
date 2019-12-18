from Module_Behavior import *

class perms (Module_Behavior):

    def start(self):
        print ("Setting up Perms Module...")

        self.mod_name = "perms"
        self.imports = ["os"]


    def load(self, csv_row):
        current_vars = self.vars
        print (csv_row["FileLocation:"])
