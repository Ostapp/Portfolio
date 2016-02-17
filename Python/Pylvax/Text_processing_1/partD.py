with open ('anagram.py') as f:
    words_src = f.read().lower().split() # cool!!

## words = text[::reduce_factor]

anagram_groups = {}

# dict is much faster than the list, so there is no need in trying to speed
# the list up

for word in words_src:
    key = "".join(sorted(word)) # sorted(word) returns a list > convert it to string
    if key not in anagram_groups:
    	anagram_groups[key] = [word]
    else:
    	anagram_groups[key].append(word)

    
##for word1 in list_words:
##    for word2 in list_words:
##        if tuple(sorted(word1)) == tuple(sorted(word2)):
##            key = "".join(tuple(sorted(word1)))
##            if key in dict_anagrams:
##                dict_anagrams[key].append(word2)
##                print("MATCH: value %s appended to key %s" % (word2, key))
##                print("%s is now %i words long" % (key, len(dict_anagrams[key])))
##            else:
##                list_value = []
##                list_value.append(word1)
##                dict_anagrams[key] = list_value
##                print("key %s is appended to dict" % key)
##                print("value %s appended to key %s" % (list_value, key))
##                dict_anagrams[key].append(word2)
##                print("value %s appended to key %s" % (word2, key))
    
# list comprehension
# [item*2 for item in list if item%2 == 1] - multiply by 2 every not equal element


### classwork
