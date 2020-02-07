import sys
#from datetime import datetime

if (sys.version_info <= (3, 0)):
  import Tkinter
else:
  import tkinter as Tkinter


class GridEditor:
    #grid_dict will be a dictionary of 2d arrays
    grid_dict = None
    #active_key is the key for the 2d array we care about.
    active_key = None


    def __init__ (self):
        empty_grid = {}
        self.set_Grid(empty_grid)

    def set_Grid(self, new_grid):
        if (type(new_grid) == dict):
            self.grid_dict = new_grid
        else:
            print ("GridEditor.set_Grid expects a dict. Got " + type(grid) + ". Making an empty grid instead.")
            empty_grid = {}
            self.grid_dict = empty_grid

    #set_active sets the active key in the grid. The Grid is a dictionary of 2d arrays.
    def set_active(self, key):
        try:
            self.grid_dict[key]
            self.active_key = key
            #print ("Active tab: " + key)
        except KeyError:
            print ("Key {} not found. Creating an empty list for key.", key)
            self.grid_dict[key] = list()
            self.active_key = key

    def get_element_at_location(self, row, col):
        return self.grid_dict[self.active_key][row][col]


    #fill_array makes an array inside of the dictionary GUI_grid in which thing
    #will be placed.
    def fill_grid(self, row, col, key, thing):
        new_array=list()

        try:
            new_array=self.grid_dict[key]
        except KeyError:
            self.grid_dict[key] = list()
            new_array=self.grid_dict[key]

        #print (key, row, col)
        for i in range (row + 1):
            try:
                new_array[i]
            except IndexError:
                new_array.append(list())

            for j in range (col + 1):
                try:
                    new_array[i][j]
                except IndexError:
                    new_array[i].append(None)

        new_array[row][col] = thing
        self.grid_dict[key] = new_array

    #Returns entry boxes adjacent to labels in dict with format:
    #label:entry
    def label_entry_dict(self):
        current_list = self.grid_dict[self.active_key]
        output = {}

        for i in current_list:
            for j in range (len(i)):
                if (isinstance(i[j], Tkinter.Label) and len(i) > j):
                    if (isinstance(i[j + 1], Tkinter.Entry)):
                        key = i[j]["text"]
                        data = i[j+1].get()
#                        output[i[j]]
                        output[key] = data
        return (output)

    #Returns entry boxes adjacent to labels in dict with format:
    #label:entry
    def label_button_dict(self):
        current_list = self.grid_dict[self.active_key]
        output = {}

        for i in current_list:
            for j in range (len(i)):
                if (isinstance(i[j], Tkinter.Label) and len(i) > j):
                    if (isinstance(i[j + 1], Tkinter.Button)):
                        key = i[j]["text"]
                        data = i[j+1]['text']
#                        output[i[j]]
                        output[key] = data
                        #print (output)
        return (output)


    def label_checkbox_dict(self):
        current_list = self.grid_dict[self.active_key]
        output = {}

        for i in current_list:
            for j in range (len(i)):
                if (isinstance(i[j], Tkinter.Label) and len(i) > j):
                    if (isinstance(i[j + 1], Tkinter.Checkbutton)):
                        key = i[j]["text"]
                        data = i[j+1]

                        print (data['variable'].get())
#                        output[i[j]]
                        output[key] = data
                        #print (output)
        return (output)

    def add_to_output(self):
        key = self.active_key
        buttons = self.label_button_dict()
        entries = self.label_entry_dict()
        checkboxes = self.label_checkbox_dict()

        output = {}
        output["type"] = key
        #output["timestamp"] = datetime.now().strftime('%m%d_%H%M%S')
        for entry in entries:
            output[entry] = entries[entry]

        for button in buttons:
            output[button] = buttons[button]

        for checkbox in checkboxes:
            output[checkbox] = checkboxes[checkbox]

        return (output)
