"""temperature"""
def main():
    """temperature"""
    num = float(input())
    txt1 = input()
    txt2 = input()
    if txt1 == "F":
        num = (num - 32)*(5/9)
    if txt1 == "K":
        num = num - 273.15
    if txt1 == "R":
        num = num*(5/9) - 273.15
    if txt2 == "F":
        num = num*(9/5) + 32
    if txt2 == "K":
        num = num + 273.15
    if txt2 == "R":
        num = (num + 273.15)*(9/5)
    print("%.2f"%num)
main()
