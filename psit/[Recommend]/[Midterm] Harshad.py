"""[Midterm] Harshad"""
def main():
    """[Midterm] Harshad"""
    num_1 = 0
    for _ in range(10):
        num = abs(int(input()))
        for i in str(num):
            num_1 += int(i)
        if num_1 == 0:
            print("No")
        elif int(num)%num_1 == 0:
            print("Yes  ")
        else:
            print("No")
        num_1 = 0
main()

