"""Point Sorting"""
def main(mylist):
    """Point Sorting"""
    for _ in range(int(input())):
        for _ in range(int(input())):
            mylist.append(tuple(input().split()))
        mylists = sorted(mylist, key=lambda x: x[1], reverse=True)
        mylist_sort = sorted(mylists, key=lambda x: int(x[0]) + int(x[1]))
        for i in mylist_sort:
            print(*i)
        mylist_sort, mylists, mylist = [], [], []
main([])

"""Point Sorting"""
def main(num1):
    """Function main"""
    lst1 = []
    for _ in range(num1):
        def ans(num3):
            """Function ans"""
            return int(num3[0]) + int(num3[1]), -int(num3[1])
        lst2 = []
        for _ in range(int(input())):
            lst2 += [input().split()]
        lst2.sort(key=ans)
        lst1 += lst2
    for i in lst1:
        print(*i)
main(int(input()))