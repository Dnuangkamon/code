"""AndAgain"""
def main():
    """ฟังก์ชั่น AndAgain"""
    list_i = []
    txt = input().replace('.', '')
    txt = txt.split()
    check = 0
    for i in txt:
        j = (i.count('a') + i.count('e') + i.count('i') + \
            i.count('o') + i.count('u'))
        if j >= 2:
            list_i.append(i)
            check += 1
        elif check == 0:
            check += 0
    if check > 0:
        print(*(sorted(list_i)), sep='\n')
    elif check == 0:
        print('Nope')
main()
