def unique_Plndr(list_Pal):

    u_Pal = ""

    for word in list_Pal:
        if word not in u_Pal:
            u_Pal = u_Pal + " " + word

    print ("unique pallindromes: " + u_Pal + '\n')