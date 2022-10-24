"""PickThemAgain"""

def main():
    """PickThemAgain"""
    list1 = input()
    list1 = list1.split()
    list2 = []
    list3 = ''
    check = 0
    for i in list1:
        for j in i:
            if j.isdigit() == True or j == '-':
                list3 += str(j)
        list2 += [list3]
        list3 = ''
    list2 = list2[::-1]
    if len(list2) > 0:
        for k in list2:
            if int(k)%3 == 0 or int(k)%5 == 0:
                print(k, end='\n')
                check += 1
    if check == 0:
        print('Nope')
main()
