""" Runner """
def main():
    """ Runner """
    distance = int(input())
    count = int(input())
    mylist = []
    total1 = 0
    total2 = 0
    answer = ""
    for _ in range(count):
        num1 = input()
        ncount = num1.find(" ")
        num2 = distance - int(num1[ncount + 1:])
        ans = int(num1[:ncount]) / num2
        num3 = num1.split()
        num4 = int(num3[-1])
        num5 = int(num3[1])
        if ((ans >= total1) and (int(num1[:ncount]) >= total2)) or ((ans <= 0) and (num4 <= 0)):
            total1 = ans
            total2 = int(num1[:ncount])
            mylist.append("%d %f" %((total2, total1)))
            answer = ("%d %f" %((total2, total1)))
        else:
            mylist.append("%d %f" %((int(num1[:ncount])), ans))
    print(int(mylist.index(answer)+1))
main()
