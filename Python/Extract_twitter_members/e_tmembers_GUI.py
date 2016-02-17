from tkinter import *
import Ostap_process_twitter_file_folder

root = Tk()

def start (event):
    t = threading.Thread(target=self._record)
    Ostap_process_twitter_file_folder.start_extraction()

def stop (event):
    exit(0) 

label1 = Label(root, text = "source folder").grid(row=0)
label2 = Label(root, text = "output folder").grid(row=1)

e_sF = Entry(root)
e_oF = Entry(root)

e_sF.grid(row=0, column=1)
e_oF.grid(row=1, column=1)

startButton = Button(root, text = "start")
startButton.grid(row=2)
startButton.bind("<Button-1>", start)  


stopButton = Button(root, text = "stop")
stopButton.grid(row=2, column=1)
stopButton.bind("<Button-1>", stop)

root.mainloop()

