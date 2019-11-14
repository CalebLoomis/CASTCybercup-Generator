from Tkinter import *
import ttk

root = Tk()
screen = Frame(root)
screen.pack()

class GuiHandler:
    global screen
    global root

    def set_title(self, title_text):
        root.title(title_text)

    def set_dimensions(self, width, height):
        root.geometry(str(width) + "x" + str(height))

    def run_code(self, cmd):
        exec(cmd)

    def pack_Label(self, pack_text):
        label = Label(screen, text=pack_text)
        label.pack()

    def newline_Button(self, pack_text):
        button = Button(screen, text=pack_text)
        button.pack()

    def newline_Button_With_Command(self, pack_text, pack_command):
        button = Button(screen, text=pack_text, command=lambda: self.run_code(pack_command))
        button.pack()

    def left_Button(self, pack_text):
        button = Button(screen, text=pack_text)
        button.pack(side=LEFT)

    def left_Button_With_Command(self, pack_text, pack_command):
        button = Button(screen, text=pack_text, command=lambda: self.run_code(pack_command))
        button.pack(side=LEFT)

    def add_tabs(self, tabs):
        tab_parent=ttk.Notebook()

            #try:
        for tab in tabs:
            new_tab = ttk.Frame(tab_parent)
            #print(tab)
            tab_parent.add(new_tab, text=tab['Name'])
        tab_parent.pack(expand=1, fill='both')


    def run(self):
        screen.mainloop()

    def stop(self):
        screen.destroy()
