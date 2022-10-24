"""Sad life of tuple"""

def main():
    """Sad life of tuple"""
    number1 = input().split() #แยกสตริง คืนค่ามาเป็น list
    number2 = input()
    number3 = number1.count(number2) #เช็คว่ามีเลขกี่ตัว
    number1 = number1.index(number2) #เช็คว่าเลขอยู่ตำแหน่งที่เท่าไหร่
    for _ in range(number3):
        print((str(number1)+' ')*number3)
main()
