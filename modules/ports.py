from Module_Behavior import *
import os

class ports (Module_Behavior):

    #Start runs once for the entire CSV File
    def start(self):
        print ("Setting up Ports Module...")

        self.mod_name = "perms"
        self.imports = ["os"]


    #Load runs once for every row in the CSV File
    def load(self, csv_row):
        current_vars = self.vars

        port_number = csv_row ["PortNumber"]
        # If it is actually true, this will be a boolean True. Otherwise False
        is_enabled = csv_row["Enabled?"] == "True"
        to_grep = ":%s " % port_number


        if is_enabled:
            output_string = "'%s' in os.popen(\"netstat -plant 2>/dev/null | grep '%s'\").read()" % (port_number, to_grep)
        else:
            output_string = "not '%s' in os.popen(\"netstat -plant 2>/dev/null | grep '%s'\").read()" % (port_number, to_grep)



        if (is_enabled):
            point_text = "Port " + port_number + " enabled"
        else:
            point_text = "Port " + port_number + " disabled"

        self.add_point(output_string, point_text)
