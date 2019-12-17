import sys

if (sys.version_info <= (3, 0)):
  from Tkinter import *
  from check_number import *
  import ttk, tkFileDialog, GridEditor, CSV_handler
else:
  from tkinter import *
  from tkinter import ttk as ttk
  from tkinter import filedialog as tkFileDialog
  from check_number import *
  import GridEditor, CSV_handler

class GuiHandler:
    ge = GridEditor.GridEditor()
    output_list = list()

    def __init__ (self):
        row_counter = 0
        col_counter = 0
        self.root = Tk()
        self.screen = Frame(self.root)
        self.screen.pack()

    #Sets the title of the window
    def set_title(self, title_text):
        self.root.title(title_text)

    def set_dimensions(self, width, height):
        self.root.geometry(str(width) + "x" + str(height))

    #Tries to execute file. Failing that, will attempt to run a cmd ad-hoc
    def run_code(self, cmd):
        try:
            with open (cmd) as c:
                code = compile(c.read(), cmd, 'exec')
                #TODO: setup run_code to accept global and local vars
                #exec(code, global_vars, local_vars)
                exec(code, globals())
        except IOError:
            try:
                exec(cmd)
            except NameError:
                print("Error. " + cmd + " not a file or python command.")

    #Run_code with knowledge of its position.
    def run_code(self, cmd, row, col):
        try:
            with open (cmd) as c:
                code = compile(c.read(), cmd, 'exec')
                #TODO: setup run_code to accept global and local vars
                #exec(code, global_vars, local_vars)
                exec(code, locals())
        except IOError:
        #    try:
                exec(cmd)
        #    except NameError:
        #        print("Error. " + cmd + " not a file or python command.")

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

    #Grid Label with parent padding and tab name specified
    def grid_Label(self, pack_text, my_row, my_col, pad_x, pad_y, parent, tab_name):
        label = Label(parent, text=pack_text)
        label.grid(row=my_row, column=my_col, padx=pad_x, pady=pad_y)
        self.ge.fill_grid(my_row, my_col, tab_name, label)

    #Grid Entry Box without parent specified
    def grid_Entry(self, my_row, my_col):
        label = Entry(self.screen)
        label.grid(row=my_row, column=my_col)

    #Grid Entry Box with parent specified
    def grid_Entry(self, my_row, my_col, parent):
        entry = Entry(parent)
        entry.grid(row=my_row, column=my_col)

    #Grid Entry Box with parent and padding specified
    def grid_Entry(self, my_row, my_col, pad_x, pad_y, parent):
        entry = Entry(parent)
        entry.grid(row=my_row, column=my_col, padx=pad_x, pady=pad_y)

    #Grid Entry Box with parent, padding and tab specified
    def grid_Entry(self, my_row, my_col, pad_x, pad_y, parent, tab_name):
        entry = Entry(parent)
        entry.grid(row=my_row, column=my_col, padx=pad_x, pady=pad_y)
        self.ge.fill_grid(my_row, my_col, tab_name, entry)

    #Grid Button without parent specified
    def grid_Button(self, pack_text, my_row, my_col):
        button = Button(self.screen, text=pack_text)
        button.grid(row=my_row, column=my_col)

    #Grid Button with parent specified
    def grid_Button(self, pack_text, my_row, my_col, parent):
        button = Button(parent, text=pack_text)
        button.grid(row=my_row, column=my_col)

    #Grid Button with both parent and padding specified
    def grid_Button(self, pack_text, my_row, my_col, pad_x, pad_y, parent):
        button = Button(parent, text=pack_text)
        button.grid(row=my_row, column=my_col, padx=pad_x, pady=pad_y)

    #Grid button with command without parent
    def grid_Button_With_Command(self, pack_text, pack_command, my_row, my_col):
        button = Button(self.screen, text=pack_text, command=lambda: self.run_code(pack_command))
        button.grid(row=my_row, column=my_col)

    #Grid button with command with parent
    def grid_Button_With_Command(self, pack_text, pack_command, my_row, my_col,parent):
        button = Button(parent, text=pack_text, command=lambda: self.run_code(pack_command))
        button.grid(row=my_row, column=my_col)

    #Grid button with command, parent and padding
    def grid_Button_With_Command(self, pack_text, pack_command, my_row, my_col, pad_x, pad_y, parent):
        button = Button(parent, text=pack_text, command=lambda: self.run_code(pack_command, my_row, my_col))
        button.grid(row=my_row, column=my_col, padx=pad_x, pady=pad_y)

    #Grid button with command, parent and padding
    def grid_Button_With_Command(self, pack_text, pack_command, my_row, my_col, pad_x, pad_y, parent, tab_name):
        button = Button(parent, text=pack_text, command=lambda: self.run_code(pack_command, my_row, my_col))
        button.grid(row=my_row, column=my_col, padx=pad_x, pady=pad_y)
        self.ge.fill_grid(my_row, my_col, tab_name, button)

    #DEPRECIATED
    def newline_Button(self, pack_text):
        print ("newline_Button DEPRECIATED")
        button = Button(self.screen, text=pack_text)
        button.pack()

    def button_With_Command(self, pack_text, pack_command):
        button = Button(self.screen, text=pack_text, command=lambda: self.run_code(pack_command))
        button.pack()

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

    #Event on tab switch
    def on_tab_selected(self, event):
        selected_tab = event.widget.select()
        tab_text = event.widget.tab(selected_tab, "text")
        self.ge.set_active(tab_text)


    def file_selection_box(self):
        #print("I've reached this point.")
        self.root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"), ("jpeg files", "*.jpeg")))
        return (self.root.filename)

    def add_tabs(self, tabs):
        tab_parent=ttk.Notebook()

            #try:
        for tab in tabs:
            new_tab = ttk.Frame(tab_parent)
            #print (tab)
            tab_file = tab['csv']
            tab_infos = CSV_handler.loadCSV(tab_file)


            for tab_info in tab_infos:
                can_create = True
                tab_type = tab_info['type'].lower()
                tab_text = tab_info['text'].title()
                tab_script = tab_info['script']
                tab_desc = tab_info['description']
                tab_name = tab['name']


                if can_create:
                    can_create = check_number(tab_info, "row", tab_file, tab_desc)
                    tab_row = int(tab_info['row'])

                if can_create:
                    can_create = check_number(tab_info, "column", tab_file, tab_desc)
                    tab_col = int(tab_info['column'])

                if can_create:
                    can_create = check_number(tab_info, "padx", tab_file, tab_desc)
                    tab_padx = int(tab_info['padx'])

                if can_create:
                    can_create = check_number(tab_info, "pady", tab_file, tab_desc)
                    tab_pady = int(tab_info['pady'])


                if (tab_type == "label" and can_create):
                    #print ("Reached Labeling")
                    self.grid_Label(tab_text, tab_row, tab_col, tab_padx, tab_pady, new_tab, tab_name)

                elif (tab_type == "entry" and can_create):
                    #print ("Reached Entry")
                    self.grid_Entry(tab_row, tab_col, tab_padx, tab_pady, new_tab, tab_name)

                elif (tab_type == "useless_button" and can_create):
                    self.grid_Button(tab_text, tab_row, tab_col, tab_padx, tab_pady, new_tab)

                elif (tab_type == "button" and can_create):
                    #print(tab_script)
                    self.grid_Button_With_Command(tab_text, tab_script, tab_row, tab_col, tab_padx, tab_pady, new_tab, tab_name)

            #print(tab)
            tab_parent.add(new_tab, text=tab_name)

        tab_parent.bind("<<NotebookTabChanged>>", self.on_tab_selected)
        tab_parent.pack(expand=1, fill='both')

    def build_label(self):
        pass

    def run(self):
        self.screen.mainloop()

    def stop(self):
        self.screen.destroy()

    def change_label(self, row, col, new_text):
        self.GUI_grid[row][col]['text'] = new_text

    def file_Button(self, row, col):
        filename = self.file_selection_box()
        button = self.ge.get_element_at_location(row, col)
        #print (self.active_key)
        button['text'] = filename

    def add_to_output(self):
        appendex = self.ge.add_to_output()
        will_append = True
        for i in self.output_list:
            if (appendex == i):
                print ("Duplicate entry found. Ignoring!")
                will_append = False
        if (will_append):
            self.output_list.append(appendex)

    def get_output(self):
        return (self.output_list)
