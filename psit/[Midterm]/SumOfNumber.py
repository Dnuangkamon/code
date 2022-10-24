""" SumOfNumber """
def main():
    """ SumOfNumber """
    num = 0
    num_1 = int(input())
    while True:
        num_2 = int(input())
        if num_2 == -1:
            print(num)
            break
        num += num_2
        if num == num_1:
            print(num)
            break
main()
