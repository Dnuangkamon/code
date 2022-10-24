""" [Midterm] Lotto """
def main():
    """ [Midterm] Lotto """
    num1 = input() #รางวัลที่ 1 เป็นตัวเลข 6 หลัก  6ล้าน
    num2 = input() #รางวัลเลขท้าย 2 ตัว เป็นตัวเลข 2 หลัก 2000
    num3 = input() #รางวัลเลขหน้า 3 ตัว รางวัลแรก เป็นตัวเลข 3 หลักา 3 ตัว 4000
    num4 = input() #รางวัลเลขหน้า 3 ตัว รางวัลสอง เป็นตัวเลข 3 หลัก 4000
    num5 = input() #รางวัลเลขท้าย 3 ตัว รางวัลแรก เป็นตัวเลข 3 หลักว 4000
    num6 = input() #เลขท้าย 3 ตัว รางวัลสอง เป็นตัวเลข 3 หลัก 4000
    number = input() #หมายเลขสลากกินแบ่งที่ซื้อมา เป็นตัวเลข 6 หลัก
    money = 0
    if number[4:7] == num2:
        money += 2000
    if number[0:3] == num3:
        money += 4000
    if number[0:3] == num4:
        money += 4000
    if number[3:7] == num5:
        money += 4000
    if number[3:7] == num6:
        money += 4000
    number1 = "1" + num1
    ans1 = (str(int(number1) - 1))
    ans2 = (str(int(number1) + 1))
    if number == num1:
        money += 6000000
    if len(ans1) >= 6 or len(ans2) >= 6:
        if number == ans1[1:7] or number == ans1:
            money += 100000
        elif number == ans2[1:7] or number == ans2:
            money += 100000
    print(money)
main()
