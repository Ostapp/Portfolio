import json
from collections import Counter

with open ('clean_words.json') as in_file:    
    text = in_file.read()
    final_words = json.loads(text)

unique_words = set(final_words)

print("there is %s total words in the text" % str(len(final_words)))
print("there is %s unique words in the text" % str(len(unique_words)))

counted_words = dict()

for word in unique_words:
    counted_words[word] = final_words.count(word)

list_counted_words = []

for key, value in counted_words.items():
    list_counted_words.append((value, key))

sorted_list_counted_words = sorted(list_counted_words, reverse = True)

print ("The top 20 most common words are %s" % sorted_list_counted_words[0:20])



##list_counted_words.sort(key = values())


##counted = Counter(final_words)
##counted.most_common(20)



#try to do without counter

#how to get least common?
#.most_common(20)[::-1] to sort in ascending order

