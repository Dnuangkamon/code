"""number"""
def number():
    """เลข"""
    name = input()
    keep = ''
    dic_name = {'A':'(56 54 45 46)', 'B':'6', 'C':'(4 11)',\
        'D':'(20 21 14)', 'E':'(54 48)', 'F':'(31 29)',\
        'G':'(1 8)', 'H':'(44 41)', 'I':'(47 71)', 'J':'8',\
        'K':'(4 1)', 'L':'(36 42)', 'M':'33', 'N':'(25 19)',\
        'O':'(58 60)', 'P':'(30 32 28 27)', 'Q':'4', 'R':'35',\
        'S':'(11 40 38 39)', 'T':'(23 21 22 24 18 16)',\
        'U':'(68 51 52)', 'V':'37', 'W':'37', 'X':'11',\
        'Y':'(34 13 71 48)', 'Z':'11'}
    for i in name:
        if i in dic_name:
            keep += (dic_name[i]+' ')
    print(keep)
number()
