
#this program creates labels in two different frames

import tkinter

class MyGUI:
    def __init__(self):
        #create the main window widget
        self.main_window = tkinter.Tk()
        
        #create two frames, one for the top and
        #one for the bottom
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        #create three label widgets for the top frame
        self.label1 = tkinter.Label(self.top_frame, text='Winken')
        self.label2 = tkinter.Label(self.top_frame, text='Blinken')
        self.label3 = tkinter.Label(self.top_frame, text='Nod')
        
        #pack the labels that are in the top frame
        #use the side='top' argument to stack them
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')
        
        #create label widgets for the bottom frame
        self.label4 = tkinter.Label(self.bottom_frame, text='Winken')
        self.label5 = tkinter.Label(self.bottom_frame, text='Blinken')
        self.label6 = tkinter.Label(self.bottom_frame, text='Nod')
        
        #pack labels that are in the bottom
        #USe the side='left' argument
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')
        
        #pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        #tkinter main loop
        tkinter.mainloop()
        
    
my_gui = MyGUI()