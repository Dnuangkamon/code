""" B - Fully pair? """
def main():
    """ฟังก์ชั่น B - Fully pair """
    txt = input()
    list_txt = ''
    while txt != '':
        position_1 = txt[0]
        count_1 = txt.count(position_1)
        if count_1%2 == 1:
            list_txt += position_1
        txt = txt.replace(position_1, '')
    if list_txt == '':
        print('fully paired')
    else:
        print(list_txt)
main()
