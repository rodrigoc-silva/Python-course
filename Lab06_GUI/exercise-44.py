
#this program converts distances in kilometers
#to miles.

import tkinter
import tkinter.messagebox

class KiloConverterGUI:
    def __init__(self):
        #create the main widget
        self.main_window = tkinter.Tk()
        
        #create two frames to group widgets
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        #create the widgets for the top frame
        self.prompt_label = tkinter.Label(self.top_frame,
                                    text='Enter the distance in Kilometers:')
        self.kilo_entry = tkinter.Entry(self.top_frame,
                                    width=10)
                                    
        #pack the top frame's widgets
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')
        
        #create a button widget.
        #The do_something method should be executed
        self.calc_button = tkinter.Button(self.main_window,
                                        text='Convert',
                                        command=self.convert)
                                        
        #create a Quit Button. When this button is clicked
        #the root widget's destroy method called
        self.quit_button = tkinter.Button(self.main_window,
                                        text='Quit',
                                        command=self.main_window.destroy)
        
        #pack the button
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        #pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        #enter tkinter main loop
        tkinter.mainloop()
        
    
    #convert method is a callback function for the button
    def convert(self):
        #get value entered by the user into the kilo_entry widget
        kilo = float(self.kilo_entry.get())
        
        #convert kilometers to miles
        miles = kilo * 0.6214
        
        #display the results in an info dialog box
        tkinter.messagebox.showinfo('Results', 'Kilometers is equal to '+
                                    str(miles) + ' miles.')
  
kilo_conv = KiloConverterGUI()   