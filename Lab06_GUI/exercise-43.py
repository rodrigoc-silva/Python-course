
#this program has a Quit button that calls
# the Tk class' destroy method when clicked

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
                                        
        #create a Quit Button. When this button is clicked
        #the rrot widget's destroy method called
        self.quit_button = tkinter.Button(self.main_window,
                                        text='Quit',
                                        command=self.main_window.destroy)
        
        #pack the button
        self.my_button.pack()
        self.quit_button.pack()
        
        #enter tkinter main loop
        tkinter.mainloop()
        
    
    #do_something method is a callback function for the button
    def do_something(self):
        #display an info dialog box
        tkinter.messagebox.showinfo('Response', 'Thanks for clicking the button')
  
my_gui = MyGUI()   