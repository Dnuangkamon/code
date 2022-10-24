"""MissingNumber"""

def main():
    """MissingNumber"""
    total = []
    check = 0
    txt = []
    number1 = int(input())
    while True:
        number = int(input())
        if number == 0:
            break
        total += [number]
    for i in range(number1):
        for j in total:
            if (i+1) == j:
                check = 1
                break
        if check == 0:
            txt += [i+1]
        check = 0
    for k in txt:
        print(k)
main()
