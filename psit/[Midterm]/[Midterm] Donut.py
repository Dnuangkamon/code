""" Donut """
def main():
    """ Donut """
    numa = int(input()) #4 #1
    numb = int(input()) #4 #1
    numc = int(input()) #3 #1
    numd = int(input()) #50 #1
    summ = numb + numc #ซื้อ+แถม #2
    count = numd // summ #จำนวนที่ต้องการ//ซื้อ+แถม(summ) #0
    count1 = numd % summ #เศษที่เหลือ #1
    if count1 == 0:
        print("%d %d" %(((count *numb) * numa), (count * summ)))
    elif count1 != 0:
        total1 = (((count+1) * numb) * numa) #1
        total2 = (((count * numb) + count1) * numa) #1
        if total1 <= total2:
            print("%d %d" %(total1, ((count + 1) * summ)))
        elif total1 > total2:
            print("%d %d" %(total2, ((count * summ) + count1)))
main()

# โดนัทราคาชิ้นละ a บาท ถ้าซื้อโดนัทจำนวน b ชิ้นด้วยกัน จะได้แถมอีก c ชิ้นฟรี ถ้าคุณต้องการได้โดนัทอย่างน้อย d ชิ้น จะต้องจ่ายเงินน้อยที่สุดกี่บาท และจะได้โดนัทจำนวนมากที่สุดทั้งหมดกี่ชิ้น

# หมายเหตุ โดนัทในรูปดูน่าอร่อยมาก

#  Specification
#  Input Specification	 Output Specification

# มี 4 บรรทัด แต่ละบรรทัดเป็นเลขจำนวนเต็ม
# a, {a > 0}
# b, {b > 0}
# c, {c >= 0}
# d, {d >= 0}

# 1 บรรทัด แสดงค่าจำนวนเงินที่ต้องจ่าย (บาท) และจำนวนโดนัทที่ได้ (ชิ้น) แยกกันโดยใช้ช่องว่าง 1 ช่อง
#  Sample Case
#  Sample Input	 Sample Output
# 5
# 3
# 1
# 8
# 30 8
# 2
# 4
# 3
# 12
# 16 14
# 1
# 1
# 1
# 1
# 1 2