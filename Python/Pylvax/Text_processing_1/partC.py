with open ('source_file.txt') as raw:
    text = raw.read()

# split the text into semicolumn separated fragments 
list_frgs = text.split(":")

# split the fragments into sentences                  
list_words_frgs = [fragment.split() for fragment in list_frgs]

suffix = ('.','!','?')           
list_sen = []                    
sentence = []  
for fragment in list_words_frgs:
    for word in fragment:        
        if word.endswith(suffix):    
           sentence.append(word)     
           list_sen.append(sentence) 
           sentence = []
        elif word is fragment[-1]:  
           if len(sentence) > 0:
               list_sen.append(sentence) 
               sentence = []
               sentence.append(word)
        else: sentence.append(word)  

print ("number of sentences in the text is " + str(len(list_sen)))

# find the longest and the shortest sentences by word count
sorted_by_word = sorted(list_sen, key = len, reverse=True)


# find the longest and the shortest sentences by char count
def in_char_length(list_of_words):
    sen_length = 0
    for word in list_of_words:
        sen_length = sen_length + len(word)
    return sen_length

sorted_by_char = sorted(list_sen, key = in_char_length, reverse=True)

# create a separate list for each type of sentences
dot_sen = []
excl_sen = []
q_sen = []

for sentence in list_sen:
    if "." in sentence[-1]:
        dot_sen.append(sentence)
    elif "?" in sentence[-1]:
        q_sen.append(sentence)
    elif "!" in sentence[-1]:
        excl_sen.append(sentence)
    else: dot_sen.append(sentence) # consider those sentences which does not end
                                   # with the punctuation marks as the 
                                   # declarative ones

print ("number of declarative sentences in the text is " + str(len(dot_sen)))
print ("number of exclamatory sentences in the text is " + str(len(excl_sen)))
print ("number of question sentences in the text is " + str(len(q_sen)))

# print out the average length for each group, based on words counts
def avg_sen_len(list_of_sentences):
    group_len = 0
    for sentence in list_of_sentences:
        group_len = group_len + len(sentence)

    avg_len = group_len / len(list_of_sentences)

    return avg_len

print("Average length for declarative sentences is " + str(avg_sen_len(dot_sen)) + " words")
print("Average length for question sentences is " + str(avg_sen_len(q_sen)) + " words")

########################***REDUNDANT CODE***############################

# transform list of strings into a string
##text_no_spkrs = "".join(" " + word for word in list_words_no_spkrs)

##i = 0
##j = 0
##
##for i in range (len(list_sen)-1):
##    for j in range (i+1, len(list_sen)-1):
##        if len(list_sen[i]) < len(list_sen[j]):
##            list_sen[i], list_sen[j] = list_sen[j], list_sen[i]
##        j += 1
##    i+=1

# create separate lists of sentences
# for sentences of different types

# remove speakers' names
## list_words_no_spkrs = [word for word in list_words
##                       if ":" not in word] 
