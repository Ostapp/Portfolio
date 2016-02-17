with open ('anagram.py') as in_file:
    text = in_file.read().lower().split() 

   words = text[::reduce_factor]