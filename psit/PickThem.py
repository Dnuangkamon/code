"""PickThem"""

def main():
    """PickThem"""
    list1 = input()
    list1 = list1.split()
    list2 = []
    list3 = ''
    check = 0
    for i in list1:
        for j in i:
            if j.isdigit() == True:
                list3 += str(j)
        list2 += [list3]
        list3 = ''
    if len(list2) > 0:
        for k in list2:
            if int(k)%2 == 0:
                print(k, end='\n')
                check += 1 #เช็คจำนวนคู่
    if check == 0:
        print('Nope')
main()
