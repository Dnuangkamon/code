"""Ink"""
def main(num):
    """Ink"""
    import math
    for _ in range(int(num[1])):
        dot = input().split()
        print(math.ceil(((3.1416)*(((int(dot[0])**2 + int(dot[1])**2)**0.5))**2)/(int(num[0]))))
main(input().split())

"""psit"""
import math
def main():
    """psit"""
    txt1 = input().split()
    mylist = []
    for i in range(int(txt1[1])):
        txt2 = input().split()
        mylist.append([int(txt2[0]), int(txt2[1])])
    for i in range(len(mylist)):
        radius = ((mylist[i][0]**2)+(mylist[i][1])**2)**0.5
        mylist[i] = 3.1416*((radius)**2)
    for i in range(len(mylist)):
        print(math.ceil(mylist[i]/int(txt1[0])))
main()