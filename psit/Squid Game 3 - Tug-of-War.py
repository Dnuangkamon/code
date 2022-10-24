"""Squid Game 3 - Tug-of-War"""

def main():
    """Squid Game 3 - Tug-of-War"""
    num_1 = 0
    num_2 = 0
    for _ in range(10):
        num_a = int(input())
        num_1 += num_a
    for _ in range(10):
        num_b = int(input())
        num_2 += num_b
    if num_1 > num_2:
        print('B')
    elif num_1 < num_2:
        print('A')
    else:
        print('AB')
main()
