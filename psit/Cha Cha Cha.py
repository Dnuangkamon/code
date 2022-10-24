"""Cha Cha Cha"""
import math
def main():
    """ฟังก์ชัน Cha Cha Cha"""
    day = int(input())
    day_1 = 0
    for _ in range(day):
        day_2 = float(input())
        day_1 += math.ceil(day_2)
    ans = 8720*day_1
    print('%d' %ans)
main()
