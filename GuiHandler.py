from Tkinter import *
import ttk, CSV_reader, tkFileDialog

GUI_grid = list()

class GuiHandler:


    def __init__ (self):
        global GUI_grid
        row_counter = 0
        col_counter = 0
        self.root = Tk()
        self.screen = Frame(self.root)
        self.screen.pack()

    def fill_array(self, row, col, thing):
        global GUI_grid
        new_array=list()
        for i in range (row + 1):
            try:
                new_array.append(GUI_grid[i])
            except:
                new_array.append(list())

            for j in range (col + 1):
                try:
                    new_array[i].append(GUI_grid[i][j])
                except:
                    new_array[i].append(None)

        new_array[row] [col] = thing
        GUI_grid = new_array

    #Sets the title of the
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
    def run_code(self, cmd, x, y):
        globals()["x_pos"] = x
        globals()["y_pos"] = y
        globals()["tkinterobj"] = self
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

    def pack_Label(self, pack_text):
        label = Label(self.screen, text=pack_text)
        label.pack()


    #Grid Label without parent specified
    def grid_Label(self, pack_text, my_row, my_col):
        label = Label(self.screen, text=pack_text)
        self.fill_array(my_row, my_col, label)
        label.grid(row=my_row, column=my_col)

    #Grid Label with parent specified
    def grid_Label(self, pack_text, my_row, my_col, parent):
        label = Label(parent, text=pack_text)
        self.fill_array(my_row, my_col, label)
        label.grid(row=my_row, column=my_col)

    #Grid Label with parent and padding specified
    def grid_Label(self, pack_text, my_row, my_col, pad_x, pad_y, parent):
        label = Label(parent, text=pack_text)
        self.fill_array(my_row, my_col, label)
        label.grid(row=my_row, column=my_col, padx=pad_x, pady=pad_y)

    #Grid Entry Box without parent specified
    def grid_Entry(self, my_row, my_col):
        label = Entry(self.screen)
        self.fill_array(my_row, my_col, label)
        label.grid(row=my_row, column=my_col)

    #Grid Entry Box with parent specified
    def grid_Entry(self, my_row, my_col, parent):
        label = Entry(parent)
        self.fill_array(my_row, my_col, label)
        label.grid(row=my_row, column=my_col)

    #Grid Entry Box with parent and padding specified
    def grid_Entry(self, my_row, my_col, pad_x, pad_y, parent):
        label = Entry(parent)
        self.fill_array(my_row, my_col, label)
        label.grid(row=my_row, column=my_col, padx=pad_x, pady=pad_y)

    #Grid Button without parent specified
    def grid_Button(self, pack_text, my_row, my_col):
        button = Button(self.screen, text=pack_text)
        self.fill_array(my_row, my_col, button)
        button.grid(row=my_row, column=my_col)

    #Grid Button with parent specified
    def grid_Button(self, pack_text, my_row, my_col, parent):
        button = Button(parent, text=pack_text)
        self.fill_array(my_row, my_col, button)
        button.grid(row=my_row, column=my_col)

    #Grid Button with both parent and padding specified
    def grid_Button(self, pack_text, my_row, my_col, pad_x, pad_y, parent):
        button = Button(parent, text=pack_text)
        self.fill_array(my_row, my_col, button)
        button.grid(row=my_row, column=my_col, padx=pad_x, pady=pad_y)

    #Grid button with command without parent
    def grid_Button_With_Command(self, pack_text, pack_command, my_row, my_col):
        button = Button(self.screen, text=pack_text, command=lambda: self.run_code(pack_command))
        self.fill_array(my_row, my_col, button)
        button.grid(row=my_row, column=my_col)

    #Grid button with command with parent
    def grid_Button_With_Command(self, pack_text, pack_command, my_row, my_col,parent):
        button = Button(parent, text=pack_text, command=lambda: self.run_code(pack_command))
        self.fill_array(my_row, my_col, button)
        button.grid(row=my_row, column=my_col)

    #Grid button with command, parent and padding
    def grid_Button_With_Command(self, pack_text, pack_command, my_row, my_col, pad_x, pad_y, parent):
        button = Button(parent, text=pack_text, command=lambda: self.run_code(pack_command, my_row, my_col))
        self.fill_array(my_row, my_col, button)
        button.grid(row=my_row, column=my_col, padx=pad_x, pady=pad_y)
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

    def file_selection_box(self):
        #print("I've reached this point.")
        self.root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        return (self.root.filename)

    def add_tabs(self, tabs):
        tab_parent=ttk.Notebook()

            #try:
        for tab in tabs:
            new_tab = ttk.Frame(tab_parent)
            #print (tab)
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

                elif (tab_type == "useless_button" and can_create):
                    self.grid_Button(tab_text, tab_row, tab_col, tab_padx, tab_pady, new_tab)

                elif (tab_type == "button" and can_create):
                    #print(tab_script)
                    self.grid_Button_With_Command(tab_text, tab_script, tab_row, tab_col, tab_padx, tab_pady, new_tab)

            #print(tab)
            tab_parent.add(new_tab, text=tab['name'])

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
