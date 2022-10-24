"""[Midterm] LargestNumber"""
def number(ans1, ans2):
    """ Number """
    if ans1 >= ans2:
        return ans1
    else:
        return ans2
def main():
    """[Midterm] LargestNumber"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    if num1 >= 0 and num2 >= 0 and num3 >= 0:
        ans_1 = "%d%d%d" %(num1, num2, num3)
        ans_2 = "%d%d%d" %(num1, num3, num2)
        ans_3 = "%d%d%d" %(num2, num1, num3)
        ans_4 = "%d%d%d" %(num2, num3, num1)
        ans_5 = "%d%d%d" %(num3, num2, num1)
        ans_6 = "%d%d%d" %(num3, num1, num2)
        ans = number(ans_1, ans_2)
        ans = number(ans, ans_3)
        ans = number(ans, ans_4)
        ans = number(ans, ans_5)
        ans = number(ans, ans_6)
        if ans == "000":
            print("0")
        else:
            print(ans)
main()
