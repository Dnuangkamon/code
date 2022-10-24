""" Muddled Menu """

def main():
    """ ฟังก์ชั่น Muddled Menu """
    mylist = []
    while 1:
        menu = input()
        if menu == 'DONE':
            break
        elif menu == 'CLOSED':
            mylist = []
            break
        elif menu == 'SOMETHING\'S WRONG':
            mylist = []
        elif 'Can\'t' in menu:
            mylist.remove(menu[10:])
        else:
            find1 = menu.find(' #')
            food = menu[:find1]
            if '#N' in menu:
                mylist.insert(len(mylist), food)
            else:
                menu1 = int(menu[find1+2:])-1
                mylist.insert(menu1, food)
    pos = mylist[::-1]
    print('Full Course:', mylist, 'Reversed:', pos)
main()
