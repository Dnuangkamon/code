"""PrasomSib"""
def main():
    """PrasomSib"""
    num = int(input())
    check = 0
    ans = 0
    for i in range(len(str(num))-1):
        check += int(str(num)[i])
        while check <= 10:
            if check == 10:
                ans += 1
                check = 0
                break
            if check != 10:
                if i+1 < len(str(num)):
                    check += int(str(num)[i+1])
                    i = i+1
                else:
                    break
            if check > 10:
                check = 0
                break"""GasStations"""
def main():
    """เขียนใหม่ด่วน"""
    numc = float(input())
    numx = float(input())
    nump = int(input())
    print(ans)
main()

"""PrasomSib"""
def main(number):
    """Function main"""
    ans = 0
    for i in range(len(number)):
        cal = 0
        for j in number[i:]:
            cal += int(j)
            if cal == 10:
                ans += 1
                break
    print(ans)
main(input())


def somsib(num):
    """https://www.youtube.com/watch?v=lV-6aaW4tO8"""
    ans = 0
    for i in range(len(num)):
        sumsib = int(num[i])
        for j in range(i+1, len(num)):
            sumsib += int(num[j])
            if sumsib == 10:
                ans += 1
                break
            elif sumsib > 10:
                break
    print(ans)
somsib(input())