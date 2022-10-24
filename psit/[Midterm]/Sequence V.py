"""Sequence V"""
def main():
    """Sequence V"""
    num = int(input())
    for i in range(num):
        print(num, end=" ")
        num -= 1
        if (i+1)%7 == 0:
            print()
main()
