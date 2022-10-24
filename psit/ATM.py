""" ATM """

def main():
    """ Input then print """
    money = int(input())
    while True:
        value = input().split()
        if value == ['END']:
            break
        if value.count('D') >= 1:
            money += int(value[1])
        elif value.count('W') >= 1:
            if money >= int(value[1]):
                money -= int(value[1])
            elif money < int(value[1]):
                money = 0
    print(money)
main()
