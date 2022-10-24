"""ฉันจะเป็น Saitama ให้ได้เลย"""
import math

def check(num1, num2):
    """ฟังก์ชันหาค่า min"""
    if num1 >= num2:
        return num1
    elif num1 <= num2:
        return num2

def main():
    """ฟังก์ชัน Saitama"""
    pushups = int(input())
    situp = int(input())
    getup = int(input())
    run = int(input())
    num_a = int(input())
    num_b = int(input())
    num_c = int(input())
    num_d = int(input())
    txt_1 = math.ceil(pushups/num_a)
    txt_2 = math.ceil(situp/num_b)
    txt_3 = math.ceil(run/num_c)
    txt_4 = math.ceil(getup/num_d)
    ans = check(txt_1, txt_2)
    ans = check(ans, txt_3)
    ans = check(ans, txt_4)
    print(ans)
main()
