import sys

if (sys.version_info <= (3, 0)):
  import Tkinter
else:
  import tkinter as Tkinter

class MyCheckbox:
    row = 0
    col = 0
    tab=""
    tkObject = None

    def __init__ (self, parent, row=None, col =None, tab_name=None):
        self.root = parent
        self.checked_var = Tkinter.BooleanVar()
        self.row = row
        self.col = col
        self.tab = tab_name
        self.tkObject = Tkinter.Checkbutton(parent, variable = self.checked_var)


    def get_obj(self):
        return self.tkObject

    def get_status(self):
        return self.checked_var.get()
