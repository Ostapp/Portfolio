from tkinter import *

class Extract_twitter_members:

    def __init__ (self, master):

        frame = Frame(master)
        frame.pack()

        
        self.input_fldr_lbl = Label (frame, text="Input Folder")
        self.input_fldr_lbl.pack(anchor=nw, side=LEFT)
                
        self.stop_button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.start_button = Button(
            frame, text="Start",
            command=self.start)
        self.start_button.pack(side=LEFT)

        #create labels

        

    def start(self):
        ...

root = Tk()

app = App(root)

root.mainloop()



