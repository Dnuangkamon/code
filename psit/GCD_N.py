"""GCD_N"""
def main():
    """GCD_N"""
    mylist = []
    ans = 0
    mylist2 = []
    for _ in range(int(input())):
        num = int(input())
        mylist.append(num)
    for i in range(max(mylist), 0, -1):
        ans = 0
        for j in mylist:
            if j%i == 0:
                ans += 1
                if ans == len(mylist):
                    mylist2.append(i)
                    break
    print(max(mylist2))
main()

"""GCD_N"""
def gcd(num1, num2):
    """GCD_N"""
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)
def main():
    """GCD_N"""
    lis = [int(input()) for i in range(int(input()))]
    ans = lis[0]
    for i in lis[1::]:
        ans = gcd(ans, i)
    print(ans)
main()