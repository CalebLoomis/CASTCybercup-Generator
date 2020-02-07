import sys

if (sys.version_info <= (3, 0)):
  import Tkinter
else:
  import tkinter as Tkinter

class MyCheckbox:
    checked_var = Tkinter.BooleanVar()
    root=Tkinter.Tk()
    row = 0
    col = 0
    tab=""
    tkObject = None

    def __init__ (self, parent=self.root, row=self.row, col = self.col, tab_name=self.tab, tkObj = self.tkObject):
        self.root = parent


    def get_obj(self):
        return tkObject

    def get_status:
        return checked_var.get()
