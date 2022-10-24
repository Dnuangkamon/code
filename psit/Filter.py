""" Flatten """
def main():
    """ Flatten """
    mylist = input()
    ans = []
    txt = ""
    for i in range(len(mylist)):
        if mylist[i].isnumeric() or mylist[i] == '-':
            txt += (mylist[i])
        else:
            if txt.isnumeric() or txt.count("-") == 1:
                ans.append(int(txt))
                txt = ''
    ans.sort(reverse=True)
    print(ans)
main()
