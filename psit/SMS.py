"""SMS"""
def main2(ans):
    """function"""
    if ans == []:
        print("null")
    else:
        print("".join(ans))

def main():
    """[SMS]"""
    ans = []
    myabc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for _ in range(int(input())):
        number = int(input())
        numk = int(input())
        if number == 1:
            for _ in range(numk):
                if ans != []:
                    ans.pop()
        if number == 2:
            ans.append(myabc[:3][numk%3-1])
        if number == 3:
            ans.append(myabc[3:6][numk%3-1])
        if number == 4:
            ans.append(myabc[6:9][numk%3-1])
        if number == 5:
            ans.append(myabc[9:12][numk%3-1])
        if number == 6:
            ans.append(myabc[12:15][numk%3-1])
        if number == 7:
            ans.append(myabc[15:19][numk%4-1])
        if number == 8:
            ans.append(myabc[19:22][numk%3-1])
        if number == 9:
            ans.append(myabc[22:][numk%4-1])
    main2(ans)
main()
