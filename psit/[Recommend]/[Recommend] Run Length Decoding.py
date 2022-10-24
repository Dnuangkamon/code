"""Run Length Decoding"""
 
def main():
    """Run Length Decoding"""
    txt = input()
    txt_1 = ''
    for i in txt:
        if not i.isalpha():
            txt_1 += i
        elif i.isalpha():
            print(i*int(txt_1), end='')
            txt_1 = ''
main()
# Run-length Decoding เป็นการถอดรหัสข้อความที่มีการเข้ารหัสโดยการรวมข้อมูลที่อยู่ใกล้เคียงกัน ที่เหมือนกัน ไว้ด้วยกัน

# ตัวอย่าง
# 5a6h7m1u7i6a
# หมายความว่ามี a อยู่ 5 ตัว
# h อยู่ 6 ตัว
# m อยู่ 7 ตัว
# u มีตัวเดียว

# โดยเมื่อถอดรหัสเสร็จแล้ว ก็จะกลายเป็น aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa

#  Specification
#  Input Specification	 Output Specification

# String ที่เข้ารหัส Run Length Encoding

# String ยาวๆ 1 บรรทัด
#  Sample Case
#  Sample Input	 Sample Output
# 5a6h7m1u7i6a
# aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa