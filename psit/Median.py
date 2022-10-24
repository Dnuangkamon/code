""" Median """
def main():
    """ ฟังก์ชั่น Median"""
    num1 = int(input())
    num3 = []
    for _ in range(num1):
        num2 = int(input())
        num3.append(num2)
        num3.sort()
    if num1%2 != 0:
        print('%.1f' %(num3[num1//2]))
    elif num1%2 == 0:
        print('%.1f' %(((num3[num1//2])+(num3[(num1//2)-1]))/2))
main()
