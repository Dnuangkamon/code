""" HW_DotE """
import math


def dot(number):
    """ ฟังก์ชั่น HW_DotE """
    if number % 2 != 0:  # n!/(n-r)!r!
        number += 1
    result = (math.factorial(number))/((math.factorial(number-(number//2)))
                                       * (math.factorial(number//2)))
    print(int(result))


dot(int(input()))
