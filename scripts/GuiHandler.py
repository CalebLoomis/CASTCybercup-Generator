from Tkinter import *
import ttk, CSV_reader



class GuiHandler:


    def __init__ (self):
        row_counter = 0
        col_counter = 0
        self.root = Tk()
        self.screen = Frame(self.root)
        self.screen.pack()



    def set_title(self, title_text):
        self.root.title(title_text)

    def set_dimensions(self, width, height):
        self.root.geometry(str(width) + "x" + str(height))

    def run_code(self, cmd):
        exec(cmd)

    def pack_Label(self, pack_text):
        label = Label(self.screen, text=pack_text)
        label.pack()


    #Grid Label without parent specified
    def grid_Label(self, pack_text, my_row, my_col):
        label = Label(self.screen, text=pack_text)
        label.grid(row=my_row, column=my_col)

    #Grid Label with parent specified
    def grid_Label(self, pack_text, my_row, my_col, parent):
        label = Label(parent, text=pack_text)
        label.grid(row=my_row, column=my_col)

    #Grid Label with parent and padding specified
    def grid_Label(self, pack_text, my_row, my_col, pad_x, pad_y, parent):
        label = Label(parent, text=pack_text)
        label.grid(row=my_row, column=my_col, padx=pad_x, pady=pad_y)

    #Grid Entry Box without parent specified
    def grid_Entry(self, my_row, my_col):
        label = Entry(self.screen)
        label.grid(row=my_row, column=my_col)

    #Grid Entry Box with parent specified
    def grid_Entry(self, my_row, my_col, parent):
        label = Entry(parent)
        label.grid(row=my_row, column=my_col)

    #Grid Entry Box with parent and padding specified
    def grid_Entry(self, my_row, my_col, pad_x, pad_y, parent):
        label = Entry(parent)
        label.grid(row=my_row, column=my_col, padx=pad_x, pady=pad_y)

    #Grid Button without parent specified
    def grid_Button(self, pack_text, my_row, my_col):
        button = Button(self.screen, text=pack_text)
        button.grid(row=my_row, column=my_col)

    #Grid Button without parent specified
    def grid_Button(self, pack_text, my_row, my_col, parent):
        button = Button(parent, text=pack_text)
        button.grid(row=my_row, column=my_col)

    def grid_Button(self, pack_text, my_row, my_col, pad_x, pad_y, parent):
        button = Button(parent, text=pack_text)
        button.grid(row=my_row, column=my_col)

    def newline_Button(self, pack_text):
        button = Button(self.screen, text=pack_text)
        button.pack()

    def button_With_Command(self, pack_text, pack_command):
        button = Button(self.screen, text=pack_text, command=lambda: self.run_code(pack_command))
        button.pack()

    def grid_Button_With_Command(self, pack_text, pack_command, my_row, my_col):
        button = Button(self.screen, text=pack_text, command=lambda: self.run_code(pack_command))
        button.grid(row=my_row, column=my_col)

    def left_Button(self, pack_text):
        button = Button(self.screen, text=pack_text)
        button.pack(side=LEFT)

    def left_Button_With_Command(self, pack_text, pack_command):
        button = Button(self.screen, text=pack_text, command=lambda: self.run_code(pack_command))
        button.pack(side=LEFT)

    def right_Button(self, pack_text):
        button = Button(self.screen, text=pack_text)
        button.pack(side=RIGHT)

    def right_Button_With_Command(self, pack_text, pack_command):
        button = Button(self.screen, text=pack_text, command=lambda: self.run_code(pack_command))
        button.pack(side=RIGHT)

    def add_tabs(self, tabs):
        tab_parent=ttk.Notebook()

            #try:
        for tab in tabs:
            new_tab = ttk.Frame(tab_parent)
            print (tab)
            tab_file = tab['csv']
            tab_infos = CSV_reader.loadCSV(tab_file)


            for tab_info in tab_infos:
                can_create = True
                tab_type = tab_info['type'].lower()
                tab_text = tab_info['text'].title()
                tab_script = tab_info['script']
                tab_desc = tab_info['description']

                try:
                    tab_row = int(tab_info['row'])
                except ValueError:
                    print ("Bad value for row in " + tab_file + " for " + tab_desc + ". Are you sure that it's a number?")
                    can_create = False

                try:
                    tab_col = int(tab_info['column'])
                except ValueError:
                    print ("Bad value for column in " + tab_file + " for " + tab_desc + ". Are you sure that it's a number?")
                    can_create = False

                try:
                    tab_padx = int(tab_info['padx'])
                except ValueError:
                    print ("Bad value for padx in " + tab_file + " for " + tab_desc + ". Are you sure that it's a number?")
                    can_create = False

                try:
                    tab_pady = int(tab_info['pady'])
                except ValueError:
                    print ("Bad value for pady in " + tab_file + " for " + tab_desc + ". Are you sure that it's a number?")
                    can_create = False

                if (tab_type == "label" and can_create):
                    #print ("Reached Labeling")
                    self.grid_Label(tab_text, tab_row, tab_col, tab_padx, tab_pady, new_tab)

                elif (tab_type == "entry" and can_create):
                    #print ("Reached Entry")
                    self.grid_Entry(tab_row, tab_col, tab_padx, tab_pady, new_tab)

                elif (tab_type == "button" and can_create):
                    self.grid_Button(tab_text, tab_row, tab_col, tab_padx, tab_pady, new_tab)

            #print(tab)
            tab_parent.add(new_tab, text=tab['name'])
        tab_parent.pack(expand=1, fill='both')


    def run(self):
        self.screen.mainloop()

    def stop(self):
        self.screen.destroy()
