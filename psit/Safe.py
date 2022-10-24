"""Safe"""
def main(code1, code2, ans):
    """ฟังก์ชั่น Safe"""
    for i in range(len(code1)):
        check = abs((ord(min(code1[i], code2[i])) - 65) + (90 - ord(max(code1[i], code2[i])))) + 1
        ans += min(abs(ord(code1[i]) - ord(code2[i])), check)
    print(ans)
main(list(input()), list(input()), 0)
