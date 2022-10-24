"""Inverter"""
def main():
    """Inverter"""
    num = input()
    ans = ""
    for i in num:
        if i == "1":
            ans += "0"
        if i == "0":
            ans += "1"
    anss = ans.lstrip("0")
    print(anss)
main()
