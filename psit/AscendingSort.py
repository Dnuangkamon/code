"""AscendingSort"""

def main():
    """AscendingSort"""
    num_max = []
    for _ in range(5):
        number = int(input())
        num_max.append(number)
        num_max.sort()
    for j in num_max:
        print(j)
main()
