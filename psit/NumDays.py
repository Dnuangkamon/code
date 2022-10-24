"""NumDays"""
from datetime import date
def main(day1, mont1, day2, mont2):
    """NumDays"""
    try:
        ans = date(2018, mont2, day2) - date(2018, mont1, day1)
        print(abs(ans.days))
    except ValueError:
        print("Impossible")
main(int(input()), int(input()), int(input()), int(input()))

"""NumDays"""
def main():
    """main function"""
    check = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, \
    7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
    day1, mday1 = int(input()), int(input())
    day2, mday2 = int(input()), int(input())
    if day1 > check[mday1] or day2 > check[mday2]:
        print("Impossible")
    else:
        allday = 0
        for i in range(mday1, mday2):
            allday += check[i]
        print(abs(allday-day1+day2))
main()