""" Is Prime Small """


def is_prime(number):
    """ Input then print"""
    i = 2
    while i <= abs(number)*0.5:
        if number % i == 0:
            return "No"
        i += 1
    return "Yes"


def main():
    """ Input then print """
    number = int(input())
    if number > 1:
        print(is_prime(number))
    else:
        print("No")


main()

# def main():
#     """prime chcek"""
#     num = int(input())
#     mylist = []
#     for i in range(1, num+1):
#         if num % i == 0:
#             mylist.append(i)
#     if len(mylist) == 2:
#         print("Yes")
#     else:
#         print("No")
