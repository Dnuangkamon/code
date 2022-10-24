'''Digit v2'''

def digit(txt):
    '''ฟังก์ชั่น Digit v2'''
    if 'thousand' in txt:
        print(4)
    elif 'hundred' in txt:
        print(3)
    elif 'ty' in txt or 'teen' in txt or 'eleven' in txt or 'twelve' in txt or 'ten' in txt:
        print(2)
    else:
        print(1)
digit(input())
