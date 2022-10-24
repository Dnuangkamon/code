"""is_prime_LARGER"""
def main(inp):
    """is_prime_LARGER"""
    prime = True
    if inp > 1:
        if inp % 2 != 0 and inp != 2:
            for i in range(3, int(inp**0.5)+1, 2):
                if inp % i == 0:
                    prime = False
                    break
        else:
            if inp == 2:
                prime = True
            else:
                prime = False
    else:
        prime = False
    print(prime)
main(int(input()))

"""psit"""
def check(num):
    """psit"""
    if num > 1:
        for i in range(1, 1+int((num**0.5)), 2):
            if num%i == 0 and i != 1:
                return False
        return True
    return False
def main():
    """psit"""
    num = int(input())
    print(check(num))
main()