"""GCD_v1"""
def main():
    """GCD_v1"""
    number_1 = int(input())
    number_2 = int(input())
    number_max = max(number_1, number_2)
    list_max = []
    for i in range(1, number_max+1):
        if number_1%i == 0 and number_2%i == 0:
            list_max.append(i)
    print(max(list_max))
main()
