""" BreachTheDoor """
def main():
    """ BreachTheDoor """
    txt = input()
    txt_list = []
    for i in txt:
        if i.isalpha() or i.isspace():
            txt_list.append(i)
        else:
            pass
    txt_1 = ''
    txt_2 = []
    for j in txt_list:
        txt_1 += j
    txt_2 = txt_1.split(' ')
    for k in txt_2:
        if len(k) > 6:
            print(k, end=' ')
main()
