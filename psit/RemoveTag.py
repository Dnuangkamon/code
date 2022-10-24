""" RemoveTag """
def main():
    """ RemoveTag """
    txt = input()
    check = 0
    check_str = ''
    for i in txt:
        if i == "<":
            check = 1
        if check == 1:
            check_str += i
        if i == '>':
            txt = txt.replace(check_str, ' ')
            check_str = ''
            check = 0
    txt_1 = txt.split()
    print(txt_1)
main()
