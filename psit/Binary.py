""" Binary1 """
def main():
    """ ฟังก์ชั่น Binary """
    decimal_num = int(input())
    list_2 = []
    decimal = decimal_num
    if decimal_num > 0:
        while decimal > 0:
            list_2.append(str(decimal % 2))
            decimal = int(decimal / 2)
        (list_2).reverse()
        print(''.join(list_2))
    elif decimal_num == 0:
        print(0)
main()
