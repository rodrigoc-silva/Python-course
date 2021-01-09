
#this program demostrates a Button widget.
#When the user clicks the button, an info
#dialog box is displayed.

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        #create the main widget
        self.main_window = tkinter.Tk()
        
        #create a button widget.
        #The do_something method should be executed
        self.my_button = tkinter.Button(self.main_window,
                                        text='Click Me!',
                                        command=self.do_something)
        
        #pack the button
        self.my_button.pack()
        
        #enter tkinter main loop
        tkinter.mainloop()
        
    
    #do_something method is a callback function for the button
    def do_something(self):
        #display an info dialog box
        tkinter.messagebox.showinfo('Response', 'Thanks for clicking the button')
  
my_gui = MyGUI()   