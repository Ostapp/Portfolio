from bs4 import BeautifulSoup
import urllib.request
import e_tmembers_GUI

# url = urllib.request.urlopen('https://hu.wikipedia.org/wiki/Magyarorsz%C3%A1g_uralkod%C3%B3inak_list%C3%A1ja') 

# filename1 = tkinter.filedialog.askopenfilename(initialdir = 'H:/Twitter_members/')

class Extractor:

        def __init__(GUI):

                GUI = e_tmembers_GUI()

                sourceFolder = GUI.e_sF.get()

                with open (sourceFolder, 'r', encoding = 'utf-8') as text:
                #url = text.read()       

                soup = BeautifulSoup(url, 'html.parser')

def tag_has_username (tag):
	if tag.has_attr('class') and not tag.has_attr('data-user-id'):
		if 'username' in tag['class']:
			return tag

for element in soup.find_all(tag_has_username):
        if element.string is not None:
                print (element.string)

