"""CoPrimeV1"""
def main():
    """CoPrimeV1"""
    number_1 = int(input())
    number_2 = int(input())
    number_max = max(number_1, number_2)
    list_max = []
    for i in range(1, number_max+1):
        if number_1%i == 0 and number_2%i == 0:
            list_max.append(i)
    list_max1 = max(list_max)
    if list_max1 == 1:
        print('YES')
    else:
        print('NO')
    print(list_max1)
main()
