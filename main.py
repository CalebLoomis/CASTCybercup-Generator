import platform
import sys, GuiHandler, CSV_handler, metahandler

def linux_distribution():
    output = False
    try:
        platform.linux_distribution()
        output = True
    except:
        print ("This scoring engine is for Linux only.", platform.system(), "detected.")

    return output


if (__name__ == "__main__"):
    TABS_FILE = 'CSV/tabs.csv'
    META_FILE = 'Engine/meta.csv'
    WIDTH = 600
    HEIGHT = 300
    TABS_LIST = CSV_handler.loadCSV(TABS_FILE)

    if linux_distribution():
        print (platform.linux_distribution())
        gui = GuiHandler.GuiHandler();
        #gui.left_Button_With_Command("Quit", "root.destroy()")
        #gui.left_Button_With_Command("Hello", "print ('test')")
        gui.set_title("Testing")
        gui.set_dimensions(WIDTH, HEIGHT)
        gui.add_tabs(TABS_LIST)
        gui.run()

        gui_output = (gui.get_output())

        mh = metahandler.metahandler(dict_list = gui_output, meta = META_FILE)
        print (mh.read_meta())

    else:
        print ("Exiting!")
