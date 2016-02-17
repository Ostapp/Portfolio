def list_list_words(list_words0):

    each_word = []

    list_words6 = []

    for word in list_words0:
        
        word = word.strip(',.":?!()$')

        if len(list_words6) == 0:

            each_word.append(word)
            list_words6.append(each_word)
            each_word = []

        else:
            for item in list_words6:

                if word in item:
                    list_words6.remove(item)
                    item.append(word)
                    list_words6.append(item)
                    
            if list_words6.index(item) == len(list_words6)-1:
                if word not in item:
                    each_word.append(word)
                    list_words6.append(each_word)
                    each_word = []

    return list_words6