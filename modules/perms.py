from Module_Behavior import *
import os

class perms (Module_Behavior):

    def start(self):
        print ("Setting up Perms Module...")

        self.mod_name = "perms"
        self.imports = ["os"]


    def load(self, csv_row):
        current_vars = self.vars

        file_location = csv_row ["FileLocation"]
        read_perms = csv_row["Read"]
        write_perms = csv_row["Write"]
        execute_perms = csv_row["Execute"]


        proper_perms = read_perms + write_perms + execute_perms

        #Some solutions require googling, and that's OK.
        current_perms = oct(os.stat(file_location).st_mode)[-3::]

        output_string = "(" + proper_perms + " == " + current_perms + ")"
        point_text = "Permissions of " + file_location
        self.add_point(output_string, point_text)
