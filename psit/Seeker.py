"""Seeker"""
def main():
    """ฟังก์ชั่น Seeker"""
    txt = input()
    list_num = ''
    check = 0
    for i in txt:
        if i.isnumeric():
            list_num += i
        else:
            list_num += i.replace(i, ' ')
    list_num = list_num.split(' ')
    for j in list_num:
        if j != '':
            check += int(j)
    print(check)
main()
