from Module_Behavior import *
import os

class perms (Module_Behavior):

    def start(self):
        print ("Setting up Perms Module...")

        self.mod_name = "perms"
        self.imports = ["os"]


    def load(self, csv_row):
        current_vars = self.vars
        try:
            file_location = csv_row ["FileLocation"]
            read_perms = csv_row["Read"]
            write_perms = csv_row["Write"]
            execute_perms = csv_row["Execute"]
            print (read_perms+write_perms+execute_perms)
            print(oct(os.stat(file_location).st_mode)[-3::])
        except KeyError:
            print ("Bad Key. Did you change the CSVs/permissions.csv file?")
