""" All_Primes """

def is_prime(number):
    """ ฟังก์ชัน All_Primes """
    i = 2
    if number > 1:
        while i <= abs(number)*0.5:
            if number % i == 0:
                return "No"
            i += 1
        return "Yes"

def main():
    """ All_Primes """
    number = int(input())
    check = ""
    result = 0
    for i in range(1, number+1):
        check = is_prime(i)
        if check == "Yes":
            result += 1
    print(result)
main()
