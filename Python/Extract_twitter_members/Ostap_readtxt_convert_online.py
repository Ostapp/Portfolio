import urllib.request
import io
import tkinter.filedialog 

#readingfile

filename = tkinter.filedialog.askopenfilename(initialdir = 'H:/Twitter_members/')

with open(filename, 'r') as url:
        text= url.read()

word = ""
goodWords = ""
goodWords1 = ""
NoDuplicates = ""       
withoutQuestions = ""
withoutNewLines = ""
nicksOnly = ""


#getting the necessary words from the text 

for char in text:
	if char is not " ":
		word = word + char
	if char is " ":
		if "@" in word:
			goodWords = goodWords + "\n" + word
			word = ""
		if "@" not in word:
			word = ""

#removing question marks
			
buf = io.StringIO(goodWords)
line = buf.readline()

for line in buf:
	line = line.replace('?',"")
	withoutQuestions = withoutQuestions + "\n" + line

#removing newlines

buf1 = io.StringIO(withoutQuestions)
line1 = buf.readline()

for line1 in buf1:
	line1 = line1.replace('\n',"")
	withoutNewLines = withoutNewLines + "\n" + line1

#getting the necessary words one more time from withoutNewlines now

word = ""
char = ""
for char in withoutNewLines:
        if char is not "\n":
                word = word + char
        if char is "\n":
            if "@" in word:
                goodWords1 = goodWords1 + "\n" + word
                word = ""
            if "@" not in word:
                    word = ""

#removing duplicates

word = ""
char = ""
for char in goodWords1:
	if char is not "\n":
		word = word + char
	if char is "\n":
		if word not in NoDuplicates:
			NoDuplicates = NoDuplicates + "\n" + word
			word = ""
		else: word = ""

#removing duplicates one more time

goodWords2 = ""
word = ""
char = ""

for char in NoDuplicates:
    if char is not "\n":
        word = word + char
    if char is "\n":
        if word not in goodWords2:
            goodWords2 = goodWords2 + "\n" + word
            word = ""
        else: word = ""

#removing duplicates one more time

goodWords3 = ""
word = ""
char = ""

for char in goodWords2:
    if char is not "\n":
        word = word + char
    if char is "\n":
        if word not in goodWords3:
            goodWords3 = goodWords3 + "\n" + word
            word = ""
        else: word = ""

# removing words not starting with @
goodWords4 = ""
word = ""
char = ""

for char in goodWords3:
    if char is not "\n":
        word = word + char
    if char is "\n":
        if len (word) >= 1:
            if word[0] != "@":
                word = ""
            else:
                if word not in goodWords4:
                    goodWords4 = goodWords4 + "\n" + word
                    word = ""
                else: word = ""
        else: word = ""

#removing commas way1
noCommas = ""
word = ""

for char in goodWords4:
    if char is not "\n":
        word = word + char
    if char is "\n":
        if len (word) >= 1:
            if word[-1] == ",":
                word = ""
            elif word[-1] != ",":
                noCommas = noCommas + "\n" + word
                word = ""
        else: word = ""

#removing dots way1
        
noDots = ""
word = ""

for char in noCommas:
    if char is not "\n":
        word = word + char
    if char is "\n":
        if len (word) >= 1:
            if word[-1] == ",":
                word = ""
            elif word[-1] != ",":
                noDots = noDots + "\n" + word
                word = ""
        else: word = ""



#removing all junk marks left in another manner
noExtraChar1 = ""
buf1 = io.StringIO(noDots)
line1 = buf1.readline()

for line1 in buf1:
	line1 = line1.replace('!',"")
	line1 = line1.replace(';',"")
	line1 = line1.replace(':',"")
	line1 = line1.replace("'s","")
	line1 = line1.replace("™","")
	line1 = line1.replace("@","")
	noExtraChar1 = noExtraChar1 + line1

#leaving only those words which do not conatin commas or dots in their middle


noExtraChar = ""

for char in noDots:
    if char is not "\n":
        word = word + char
    if char is "\n":
            if "." in word:
                word = ""
            elif "," in word:
                word = ""
#remowing all junk marks in a different manner
            elif "'s" in word:
                word = word.replace("'s","")
                noExtraChar = noExtraChar + "\n" + word ; word = ""
                
            elif ";" in word:
                word = word.replace(";","")
                noExtraChar = noExtraChar + "\n" + word ; word = ""
                
            elif ":" in word:
                word = word.replace(":","")
                noExtraChar = noExtraChar + "\n" + word ; word = ""
                
            elif "™" in word:
                word = word.replace("™","")
                noExtraChar = noExtraChar + "\n" + word ; word = ""
                
            elif "@" in word:
                word = word.replace("@","")
                noExtraChar = noExtraChar + "\n" + word ; word = ""
                
            elif "…" in word:
                word = word.replace("…","")
                noExtraChar = noExtraChar + "\n" + word ; word = ""
                
            elif "'" in word:
                word = word.replace("'","")
                noExtraChar = noExtraChar + "\n" + word ; word = ""
                
            else: noExtraChar = noExtraChar + "\n" + word ; word = ""
        
i = 0
for char in noExtraChar:
	if char == "\n":
		i = i+1



print("Total number of members is " + str(i))

#save in file
new_filename = tkinter.filedialog.asksaveasfilename(initialdir = 'H:/Twitter_members/')
new_file = open (new_filename, 'w')
new_file.write(noExtraChar)
new_file.close()
url.close()
