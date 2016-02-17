import tkinter.filedialog 

#readingfile

filename = tkinter.filedialog.askopenfilename(initialdir = 'H:/Twitter_members/')

with open(filename, 'r') as url:
        text0 = url.read()

udata=text0.decode("utf-8")
text=udata.encode("ansi","ignore")

#save in file

new_filename = tkinter.filedialog.asksaveasfilename(initialdir = 'H:/Twitter_members/')
new_file = open (new_filename, 'w')
new_file.write(text)
new_file.close()
url.close()
