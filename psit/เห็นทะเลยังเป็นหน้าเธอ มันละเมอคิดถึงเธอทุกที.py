"""ทะเล"""
def main():
    """ฉลาม"""
    shark = input()
    keep = ''
    dic_shark = {'BULL SHARK':'THE SHALLOW ZONE',\
        'GREAT WHITE SHARK':'THE TWILIGHT ZONE',\
        'CHAIN CATSHARK':'THE TWILIGHT ZONE',\
        'BLUE SHARK':'THE TWILIGHT ZONE',\
        'GUMMY SHARK':'THE TWILIGHT ZONE',\
        'MAKO SHARK':'THE TWILIGHT ZONE',\
        'FRILLED SHARK':'THE MIDNIGHT ZONE',\
        'GOBLIN SHARK':'THE MIDNIGHT ZONE',\
        'SIXGILL SHARK':'THE MIDNIGHT ZONE',\
        'GREENLAND SHARK':'THE MIDNIGHT ZONE',\
        'COOKIECUTTER SHARK':'THE MIDNIGHT ZONE',\
        'MEGAMOUTH SHARK':'THE ABYSSAL ZONE'}
    for j in dic_shark.keys():
        if shark == j:
            keep = dic_shark[shark]
    if keep != '':
        print(keep)
    else:
        print('ZONE JAI MA KLUNG RAK DUAY KAN MAI.')
main()
