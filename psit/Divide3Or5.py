""" Divide3Or5 """

def main():
    """ Divide3Or5 """
    number = int(input())
    check = 0
    for i in range(1, number+1):
        if i%3 == 0 or i%5 == 0:
            check += i
    print(check)
main()
