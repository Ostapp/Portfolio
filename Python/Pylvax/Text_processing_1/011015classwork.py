   #put defs on the top always

with open ('source_file.txt') as raw:
    text = raw.read()

l_text = text.lower()               # text lowercased

ls_text = l_text.replace('\n', ' ') # text lowercased and newlines removed

list_words = ls_text.split(' ')     # create a list of words out of text lowercased and newlines removed



list_words1 = []                    # list of words made of list_words with ,.":?!()$ chars stripped

for word in list_words:             # remove commas, dots apostrophes and "'s" 
    if word != '':                  # create a new list                             
        word = word.strip(',.":?!()$')   # for loops read only in list, they do not modify lists
        list_words1.append(word)

list_words2 = []                    # list of wors made of list_words1 with ,.":?!()$ stripped and words containing no alpha chars removed

for word in list_words1:            # Leaves only Alphabets
    if word.isalpha():
        list_words2.append(word)

list_pal = []                       # list of palyndromes made of list_words2

for word in list_words2:            # make a list of palyndromes
    if len(word) < 2:
        continue

    if is_pal(word):
        list_pal.append(word)       
        

for word in list_words:             
    if word == '': continue
    if word.isalpha() == False: continue                                            
        word = word.strip(',.":?!()$')  
        lst_wrds_alphstrp.append(word)

def print_all_Plndrs(Pal):
            
    print("all pallindromes: " + Pal + '\n')





# to get unique items in a list I should convert it to set