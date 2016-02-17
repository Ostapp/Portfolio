from bs4 import BeautifulSoup
import urllib.request
import tkinter

#url = urllib.request.urlopen('H:/Twitter_members/WeloverProject_iftt-3dprinting_members.html') 

#filename1 = tkinter.filedialog.askopenfilename(initialdir = 'H:/Twitter_members/')


def extract_members(item):

        filename = item
        print("The file " + filename + " is now being processed")
        
        members_list = ""
             
        with open (item, 'r', encoding = 'utf-8') as text:
                url = text.read()       

        soup = BeautifulSoup(url, 'html.parser')

        def tag_has_username (tag):
                if tag.has_attr('class') and not tag.has_attr('data-user-id'):
                        if 'username' in tag['class']:
                                return tag
        i = 0

        for element in soup.find_all(tag_has_username):
                if element.string is not None: # check if the element is not None
                        element.string = element.string[1:] # removing "@" character from the username
                        if (element.string not in members_list): # checking if the username is already in the list
                                members_list = members_list + "\n" + element.string # add the username to the list
                                print(element.string) # print the username
                                i = i+1
                                
        print("Total number of members is " + str(i))

        # final_filename = filename[19:-5]
        final_filename = filename[:-5] + "_final_members_list.txt"
        print("List of members saved at " + final_filename)

        new_file = open (final_filename, 'a')
        new_file.write(members_list)
        new_file.close()
        
