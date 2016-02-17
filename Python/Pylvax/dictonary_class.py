colors_list = ['blue', 'blue', 'green', 'yellow', 'blue', 'green', 'red']
    
#list.count
def count_colors_julcsi(colors_list):
    counts = dict()
    for color in color_list:
        counts[color] = colors_list.count(color)
    return counts

def count_color_1(color_list):
    counts = dict()
    for color in set(colors_list): # set will make it faster
        counts[color] = colors_list.count(color)
    return counts

# keys: .keys()
# values: .values()
# (key, value): .items()

# value sample_dict['a']
# not existing -> key error
# 
# with .get(): no KeyError, None
# sample_dict.get('a', 'hello') -> if nto ound returns hello

#dict.get
def count_colors_get(colors_list):
    counts - dict()
    for color in colors_list:
        counts[color] = counts.get(color, 0) + 1
        print counts
    return counts

# dict :set_default check if the key in the dict and returns its value
#       but if the value is not in the key it sets the value for it

def count_color_set_defaults(colors_list):
    counts = dict()
    for color in color_list:
        color_list.setdefault(color, 0)
        counts[color] += 1

# list from keys
def count_colors_from_keys(colors_list):
    counts = dict.fromkeys(colors_list, 0)
    for color in colors_list:
        counts[color] += 1
    return counts


# .fromkeys creates a dict from element using its values as keys
# list: .pop removes and returns one element from the end of the list