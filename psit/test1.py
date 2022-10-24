""" Hello """
def main():
    """ function 113 """
    number = input()
    while number.find('113') != -1:
        ans = number.find('113')
        number = number[:ans]+number[ans+3:]
    print(number)
main()
