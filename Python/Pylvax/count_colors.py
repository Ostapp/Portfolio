colors_list = ['blue', 'blue', 'green', 'yellow', 'blue', 'green', 'red']

def count_colors(colors_list):
    
    dict_colors = {}
    list_col = []
    
    for color1 in color_list:
        for color2 in color_list:
            if color1 == color2:
                if color1 in dict_colors:
                    dict_colors[color1].append([color1])
                if color1 not in dict(colors
    

def count_colors_julcsi(colors_list):
    counts = dict()
    for color in color_list:
        counts[color] = colors_list.count(color)
    return counts

def count_color_1(color_list):
    counts = dict()
    for color in colors_list:
        counts[color[ = colors_list.count(color)
    return counts

                      
