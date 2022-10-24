"""Discount"""
def main():
    """Discount"""
    mylist = []
    ans = 0
    while 1:
        price = input()
        if price == "ENTER":
            break
        mylist.append(int(price))
    mylist.sort()
    if len(mylist) <= 5:
        for i in mylist:
            ans += i
    if 5 < len(mylist) <= 11:
        for i in range(1, len(mylist)):
            ans += mylist[i]
    if 12 <= len(mylist) < 20:
        for i in range(2, len(mylist)):
            ans += mylist[i]
    if len(mylist) == 20:
        for i in range(4, len(mylist)):
            ans += mylist[i]
    if len(mylist) > 20:
        start = len(mylist)//5
        for i in range(start, len(mylist)):
            ans += mylist[i]
    print(ans)
main()
