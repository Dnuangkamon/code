"""LastStand"""

def main():
    """LastStand"""
    list1 = input()
    list1 = list1.replace(',', ' ')
    list1 = list1.replace('[', '')
    list1 = list1.replace(']', '')
    list1 = list1.split()
    list2 = []
    list3 = ''
    for i in list1:
        for j in i:
            if j.isdigit() == True:
                list3 += str(j)
        list2 += [list3]
        list3 = ''
    if len(list2) > 0:
        for k in list2:
            k = k[-1]
            print(k, end='\n')
main()

# """LastStand"""
# def main(txt):
#     """LastStand"""
#     for i in txt:
#         print(i[len(i)-1:])
# main(input().strip("[").strip("]").replace(",", " ").split())
