"""Gram_v1"""
def main():
    """Gram_v1"""
    txt = input()
    mylist = []
    mylist2 = []
    mylist3 = []
    for i in range(len(txt)-1):
        txt1 = txt[i:i+2]
        mylist.append(txt1)
    for j in mylist:
        if j not in mylist3:
            mylist3.append(j)
    for k in mylist3:
        mylist2.append(mylist.count(k))
    print(mylist3[mylist2.index(max(mylist2))])
    print(max(mylist2))
main()
