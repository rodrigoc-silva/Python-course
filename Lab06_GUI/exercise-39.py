
#this program displays a label with text

import tkinter

class MyGUI:
    def __init__(self):
        #create the main window widget
        self.main_window = tkinter.Tk()
        
        #create a label widget containing the text "hello world!"
        self.label = tkinter.Label(self.main_window, 
                                text='Hello World!')
        
        #call the label widget's pack method
        self.label.pack()
        
        #enter the tkinter main loop
        tkinter.mainloop()
    
my_gui = MyGUI()    