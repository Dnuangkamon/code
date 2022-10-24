"""" Area """
def area():
    """" ฟังก์ชั่น Area """
    num = int(input())
    count = ""
    for _ in range(num):
        area1 = input().replace(" ", "")
        count += area1
    print(len(count))
area()
