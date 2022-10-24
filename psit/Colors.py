""" Colors """

def colors(color_1, color_2):
    """ ฟังก์ชั่น Colors """
    list_color = []
    list_color.append(color_1)
    list_color.append(color_2)
    if ('Red' in list_color) and ('Yellow' in list_color):
        print('Orange')
    elif ('Blue' in list_color) and ('Yellow' in list_color):
        print('Green')
    elif ('Blue' in list_color) and ('Red' in list_color):
        print('Violet')
    elif ((color_1 == color_2) and color_1 == 'Red')\
        or ((color_1 == color_2) and color_1 == 'Yellow')\
        or ((color_1 == color_2) and color_1 == 'Blue'):
        print(color_1)
    else:
        print('Error')
colors(input().capitalize(), input().capitalize())
