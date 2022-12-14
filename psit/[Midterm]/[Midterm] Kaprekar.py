"""[Midterm] Kaprekar"""
 
def kapreka():
    """[Midterm] Kaprekar"""
    num = input()
    count = 0
    while num != "6174":
        count += 1
        num_1 = ''
        for _ in range(4):
            most_1 = 0
            for i in num:
                if int(i) > most_1:
                    most_1 = int(i)
            num_1 += str(most_1)
            check = num.find(str(most_1))
            num = num[:check]+num[check+1:]
        num = '%04d' %(int(num_1)-int(num_1[::-1]))
    print(count)
kapreka()

# Kaprekar's Constant หรือเลข 6174 คือ ค่าคงที่ของการนำตัวเลขโดด 4 ตัวที่มีอย่างน้อย 2 ตัวเลขที่แตกต่างกันมาเรียงกันตามจำนวนจากมากไปน้อยและนำมาลบกับจำนวนที่เรียงกันจากน้อยไปมาก และทำซ้ำๆไปเรื่อยๆจะได้ค่าสุดท้ายเป็น 6174 เสมอ โดยอธิบายเป็นลำดับขั้นตอนอย่างละเอียด ดังต่อไปนี้
# 1. เลขโดด 4 ตัวเรียงกัน (4-digit number) ซึ่งมีอย่างน้อย 2 ตัวที่แตกต่างกัน (สามารถเป็นเลขที่มีศูนย์นำหน้าได้)
# 2. สลับตัวเลขให้เป็นเลข 4 หลัก 2 ชุด โดยชุดแรกเป็นเลขที่เรียงจากมากไปน้อย และชุดถัดมาเป็นตัวเลขที่เรียงจากน้อยไปมาก
# 3. นำจำนวนทั้งสองมาลบกัน โดยให้จำนวนที่มากกว่าเป็นตัวตั้ง 
# 4. ทำซ้ำตั้งแต่ข้อ 2. ไปเรื่อยๆ  (กรณีผลลัพธ์ในข้อ 3 มีไม่ครบ 4 หลัก สามารถเติมศูนย์เข้าไปเพื่อให้ครบ 4 หลัก)
# ผลลัพธ์สุดท้ายจะได้ 6174 เสมอ

# อ่านแล้วอาจจะยังไม่ค่อยเข้าใจมาลองดูตัวอย่างกันดีกว่า...
# ตัวอย่าง: 3781
# ครั้งที่ 1: 8731 - 1378 = 7353
# ครั้งที่ 2: 7533 - 3357 = 4176
# ครั้งที่ 3: 7641 - 1467 = 6174

# จากข่อมูลข้างต้น หากให้จำนวน n ซึ่งเป็นเลขโดด 4 หลัก อยากทราบว่าจะต้องใช้การคำนวณกี่ครั้งเพื่อที่จะได้ผลลัพธ์เป็น 6174

#  Specification
#  Input Specification	 Output Specification

# 1 บรรทัด เป็นเลขโดด 4 หลัก

# จำนวนครั้งที่ใช้ในการคำนวณตาม Kaprekar's constant
#  Sample Case
#  Sample Input	 Sample Output
# 3781
# 3
# 4544
# 5
