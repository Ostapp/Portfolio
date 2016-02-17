def freq_Plndr(list_Pal):

    dict_ = {}

    l_dict_ = []

    for word in list_Pal:
        if word not in dict_:
            dict_[word] = ''
        if word in dict_:
            dict_[word] = dict_[word] + "*"

    print('\n' + 'pallindrome frequencies: ')
    for key, value in dict_.items():

          print (str(key) + " " + str(value))