"""CoinChangev1"""
def main():
    """CoinChangev1"""
    num = int(input()) #111
    num1 = num//25 #4 #100
    num2 = (num%25)//10 #1
    num3 = (num%25)%10//5
    num4 = num - (num1*25+num2*10+num3*5)
    print(num1+num2+num3+num4)
main()
