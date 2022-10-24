""" 3nPlus1 """

def main():
    """ 3nPlus1 """
    while True:
        number = int(input())
        check = 1
        if number == 0:
            break
        while number != 1:
            if number%2 == 0:
                number = number/2
            elif number%2 != 0:
                number = (number*3)+1
            check += 1
        print(check)
main()
