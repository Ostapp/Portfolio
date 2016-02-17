import json

def is_pal(word):
    return word == word[::-1]

with open ('source_file.txt') as raw:
    text = raw.read()

l_text = text.lower()               
list_words = l_text.split()

##content = re.sub('\s+', ' ', content)  # condense all whitespace
##content = re.sub('[^A-Za-z ]+', '', content)  # remove non-alpha chars
##words = content.split()

list_words_clean = []

for word in list_words:             
    if word == '':
        continue 
    if not word.isalpha():
        continue
    if len(word) < 2:
        continue

    word = word.strip(',.":?!()$')
    list_words_clean.append(word) 

with open('clean_words.json', 'w') as outfile:
    json_str = json.dumps(list_words_clean)
    outfile.write(json_str)

list_pal = [] 

for word in list_words_clean:      
    if len(word) < 2:
        continue

    if is_pal(word):
        list_pal.append(word)

unique_pals = set(list_pal)
