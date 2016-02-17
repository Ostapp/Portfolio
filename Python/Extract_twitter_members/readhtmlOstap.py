import urllib.request
import io
import tkinter.filedialog 


#readingfile
filename = tkinter.filedialog.askopenfilename()

url = open (filename, 'r')

text = url.read()

word = ""
wordLines = ""
wordLinesNoDuplicates = ""
wordLinesNoDuplicates_NoQuotations = ""
nicksOnly = ""

#getting the necessary words from the text 
for char in text:
	if char is not " ":
		word = word + char
	if char is " ":
		if "data-screen-name" in word:
			wordLines = wordLines + "\n" + word
			word = ""
		if "data-screen-name" not in word:
			word = ""
#removing duplicates
for char in wordLines:
	if char is not "\n":
		word = word + char
	if char is "\n":
		if word not in wordLinesNoDuplicates:
			wordLinesNoDuplicates = wordLinesNoDuplicates + "\n" + word
			word = "";
		else: word = "";

#removing quotation marks
buf = io.StringIO(wordLinesNoDuplicates)
line = buf.readline()

for line in buf:
	line = line.replace('"',"")
	wordLinesNoDuplicates_NoQuotations = wordLinesNoDuplicates_NoQuotations + "\n" + line

#removing everything except of nicknames
buf1 = io.StringIO(wordLinesNoDuplicates_NoQuotations)
line1 =  buf1.readline()

for line1 in buf1:
	line1 = line1.replace("data-screen-name=", "")
	nicksOnly = nicksOnly + line1

#save in file
new_filename = tkinter.filedialog.asksaveasfilename()
new_file = open (new_filename, 'w')
new_file.write(nicksOnly)
new_file.close()
url.close()
