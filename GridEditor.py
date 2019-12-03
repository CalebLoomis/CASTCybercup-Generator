from Tkinter import *
import ttk, CSV_reader, tkFileDialog

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
            print ("Active tab: " + key)
        except KeyError:
            print ("Key {} not found. Creating an empty list for key.", key)
            self.grid_dict[key] = list()
            self.active_key = key

    def file_Button(self, row, col):
        filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"), ("jpeg files", "*.jpeg")))
        grid = self.grid_dict
        key = self.active_key
        #print (self.active_key)
        grid[key][row][col]['text'] = filename

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
            except:
                new_array.append(list())

            for j in range (col + 1):
                try:
                    new_array[i][j]
                except:
                    new_array[i].append(None)

        new_array[row][col] = thing
        self.grid_dict[key] = new_array
