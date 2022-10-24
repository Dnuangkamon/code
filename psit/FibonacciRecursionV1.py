"""FibonacciRecursionV1"""
def main(number):
    """FibonacciRecursionV1"""
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return main(number-1) + main(number-2)
print(main(int(input())))

#code 1
    # number = int(input())
    # print(int((1+number)*(number/2)))
#code 2
    # number = int(input())
    # check = 0
    # for i in range(1, number+1):
    #     check += i
    # print(check)
    