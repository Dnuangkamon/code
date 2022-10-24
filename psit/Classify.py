"""classify"""

def main(list_txt):
    """ฟังก์ชั่น classify"""
    while True:
        txt = input()
        if txt == 'END':
            break
        list_txt += [[txt[:2], int(txt[2:4])]]
    list_txt.sort()
    year_str, branch = 0, 0
    for i in list_txt:
        num_stu = list_txt.count(i)
        year, branch1 = i[0], i[1]
        if year == year_str and branch1 == branch:
            continue
        if year == year_str:
            print('--', branch1, num_stu)
        else:
            print(year, branch1, num_stu)
        year_str, branch = year, branch1
main([])
