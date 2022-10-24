"""isPrime_large"""
def main(num):
    """isPrime_large"""
    if num == 1:
        return "NO"
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return "NO"
    return "YES"
print(main(int(input())))

"""isprime_small"""
def main():
    """isprime_small"""
    int_num = int(input())
    if int_num > 1:
        for i in range(2, 1+int((int_num**0.5))):
            if int_num%i == 0:
                print("NO")
                break
        else:
            print("YES")
    else:
        print("NO")
main()