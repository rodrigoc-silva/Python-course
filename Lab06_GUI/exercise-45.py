
#this program converts distances in kilometers
#to miles. The result displays in a label on the main window.

import tkinter

class KiloConverterGUI:
    def __init__(self):
        #create the main widget
        self.main_window = tkinter.Tk()
        
        #create three frames to group widgets
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        
        #create the widgets for the top frame
        self.prompt_label = tkinter.Label(self.top_frame,
                                    text='Enter the distance in Kilometers:')
        self.kilo_entry = tkinter.Entry(self.top_frame,
                                    width=10)
                                    
        #pack the top frame's widgets
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')
        
        #create the widget for the middle frame
        self.descr_label = tkinter.Label(self.mid_frame,
                                    text='Converted to miles:')
        
        #we nned a StringVar object to associate with an output label.
        #Use the object's set method to store a string of blank chracters.
        self.value = tkinter.StringVar()
        
        #create a label and associate it with the StringVar object.
        #Any value stored in the StringVar object will be displayed in the label.
        self.miles_label = tkinter.Label(self.mid_frame,
                                    textvariable=self.value)
                                    
        #pack the middle frame's widgets
        self.descr_label.pack(side='left')
        self.miles_label.pack(side='left')
        
        #create a button widget.
        #The do_something method should be executed
        self.calc_button = tkinter.Button(self.bottom_frame,
                                        text='Convert',
                                        command=self.convert)
                                        
        #create a Quit Button. When this button is clicked
        #the root widget's destroy method called
        self.quit_button = tkinter.Button(self.bottom_frame,
                                        text='Quit',
                                        command=self.main_window.destroy)
        
        #pack the button
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        #pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        
        #enter tkinter main loop
        tkinter.mainloop()
        
    
    #convert method is a callback function for the button
    def convert(self):
        #get value entered by the user into the kilo_entry widget
        kilo = float(self.kilo_entry.get())
        
        #convert kilometers to miles
        miles = kilo * 0.6214
        
        #convert miles to a string and store it in the StringVar object.
        #This will update the miles_label widget.
        self.value.set(miles)
  
kilo_conv = KiloConverterGUI()   