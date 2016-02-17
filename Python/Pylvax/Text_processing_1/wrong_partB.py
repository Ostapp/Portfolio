with open ('source_file.txt') as raw:
    text = raw.read()

l_text = text.lower()               
list_words = l_text.split()  

list_words_clean = []
for word in list_words:             
    if word == '':
        continue 
    if not word.isalpha():
        continue

    word = word.strip(',.":?!()$')
    list_words_clean.append(word) 


unique_words = set(list_words_clean)

dic_words = {}

for word in unique_words:
    list_words.count(word)
    dic_words[list_words.count(word)] = word




def words_count(list_words):

    each_word = []
    list_words_final = []

    for word in list_words:
        word = word.strip(',.":?!()$')

        if len(list_words_final) == 0:
            each_word.append(word)
            list_words_final.append(each_word)
            each_word = []

        else:
            for item in list_words_final:

                if word in item:
                    list_words_final.remove(item)
                    item.append(word)
                    list_words_final.append(item)
                    
            if list_words_final.index(item) == len(list_words_final)-1:
                if word not in item:
                    each_word.append(word)
                    list_words_final.append(each_word)
                    each_word = []

    return list_words_final

def sort_by_len(counted_words):

    i = 0
    j = 0

    for i in range (len(counted_words)-1):
        for j in range (i+1, len(counted_words)-1):
            if len(counted_words[i]) < len(counted_words[j]):
                counted_words[i], counted_words[j] = counted_words[j], counted_words[i]
            j += 1
        i += 1

    return counted_words

def print_20(sorted_words):

    for item in sorted_words[:21]:
        print (str(sorted_words.index(item)) + " " + item[0])

counted_words = words_count(list_words)
sorted_words = sort_by_len(counted_words)

print_20(sorted_words)