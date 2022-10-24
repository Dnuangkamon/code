"""Matrix_MN"""
def main(num1, num2, ans):
    """Matrix_MN"""
    for _ in range(num1*num2):
        num = int(input())
        ans += str(num)+" "
        if ans.count(" ")%num2 == 0:
            print(ans)
            ans = ""
main(int(input()), int(input()), "")
