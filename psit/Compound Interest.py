"""Compound Interest"""
def main(num1, num2, num3):
    """Compound Interest"""
    for _ in range(num3):
        num1 *= (1+(num2/100))
    print("%.2f"%num1)
main(int(input()), float(input()), int(input()))


"""Compound Interest"""
def main():
    """Function Compound Interest"""
    money = int(input())
    itr = float(input()) #interest
    year = int(input())
    if money == 0:
        print('0.00')
    elif itr == 0 or year == 0:
        print('%.2f' %money)
    else:
        cal = money*(1+(itr/100))**year
        print("%.2f" %cal)
main()