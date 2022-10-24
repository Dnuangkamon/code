"""Kangaroo"""

def main():
    """ Input then print """
    list_value = [int(input()), int(input()), int(input())]
    sort_value = sorted(list_value)

    different_a = sort_value[1]-sort_value[0]
    different_b = sort_value[2]-sort_value[1]

    if different_a < different_b:
        print(sort_value[2]-(sort_value[1]+1))
    else:
        print((sort_value[1]-1)-sort_value[0])
main()

# """Kangaroo"""
# def main(num1, num2, num3):
#     """Kangaro"""
#     ans = num3-num2-1
#     if num3-num2 == 1:
#         ans = num2-num1-1
#     print(ans)
# main(int(input()), int(input()), int(input()))
