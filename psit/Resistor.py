"""Resistor"""

def resistor(keep_1, keep_2, keep_3, keep_4):
    """ฟังก์ชั่น Resistor"""
    color_1 = input()
    color_2 = input()
    multiplier = input()
    tolerance = input()
    dic_1 = {'Black':'0', 'Brown':'1', 'Red':'2', 'Orange':'3', 'Yellow':'4',\
        'Green':'5', 'Blue':'6', 'Purple':'7', 'Grey':'8', 'White':'9'}
    dic_2 = {'Black':'1', 'Brown':'10', 'Red':'100', 'Orange':'1000', 'Yellow':'10000',\
        'Green':'100000', 'Blue':'1000000', 'Purple':'10000000', 'Gold':'0.1', 'Silver':'0.01'}
    dic_3 = {'Brown':'1', 'Red':'2', 'Green':'0.5', 'Blue':'0.25', 'Purple':'0.10', 'Grey':'0.05',\
        'Gold':'5', 'Silver':'10'}
    for i in dic_1.keys():
        if color_1 == i:
            keep_1 = dic_1[color_1]
        if color_2 == i:
            keep_2 = dic_1[color_2]
    for j in dic_2.keys():
        if multiplier == j:
            keep_3 = dic_2[multiplier]
    for k in dic_3.keys():
        if tolerance == k:
            keep_4 = dic_3[tolerance]
    if keep_1 != '' and keep_2 != '' and keep_3 != '' and keep_4 != '':
        print('%.4f' %((float(keep_1+keep_2)*float(keep_3)) - \
            (((float(keep_1+keep_2)*float(keep_3))/100)*float(keep_4))))
        print('%.4f' %((float(keep_1+keep_2)*float(keep_3)) + \
            (((float(keep_1+keep_2)*float(keep_3))/100)*float(keep_4))))
    else:
        print('Error')
resistor('', '', '', '')
