"""[Midterm] Stair"""
def main():
    """[Midterm] Stair"""
    num_high = int(input()) #จำนวนก้าวที่สามารถก้าวได้ยาวที่สุด
    num_stair = int(input()) #จำนวนขั้นบันได
    num_check = 0
    num_count = 0
    for _ in range(num_stair):
        num = int(input())
        if num > num_high:
            print('NO')
            break
        if num_check + num <= num_high:
            num_check += num
        elif num_check + num > num_high:
            num_count += 1
            num_check = num
    if num <= num_high:
        if num_check != 0 and num_check <= num_high:
            num_count += 1
        print(num_count)
main()

# บันไดระหว่างชั้น 1 กับชั้น 2 มีอยู่ n ขั้น แต่ละขั้นอาจจะมีความสูงไม่เท่ากัน (x1, x2, x3, ..., xn) เซนติเมตร  
# ถ้าคนสามารถเดินก้าวขึ้นได้หลายขั้นได้ในก้าวเดียว แต่ต้องมีความสูงรวมไม่เกิน y เซนติเมตร ถ้าต้องขึ้นบันไดจากชั้น 1 ไปชั้น 2 
# โดยใช้จำนวนก้าวน้อยที่สุด จะต้องก้าวทั้งหมดกี่ก้าว และถ้าไม่สามารถขึ้นไปชั้น 2 ได้ ให้ตอบ NO

#  Specification
#  Input Specification	 Output Specification

# บรรทัดที่ 1: ความสูงที่มากที่สุดที่คนสามารถก้าวได้ใน 1 ก้าว (y) เซนติเมตร เป็นจำนวนเต็มบวกหรือ 0
# บรรทัดที่ 2: จำนวนขั้น n เป็นจำนวนเต็มบวก
# บรรทัดที่ 3 ถึง n+2: ความสูงของบันไดในแต่ละขั้น  (x1 ถึง xn) เซนติเมตร เป็นจำนวนเต็มบวก
 

# 1 บรรทัด จำนวนก้าวที่น้อยที่สุดที่ใช้ในการขึ้นจากชั้น 1 ไปชั้น 2 ได้ เป็นจำนวนเต็มบวกหรือศูนย์ ถ้าไม่สามารถขึ้นไปชั้น 2 ได้ ให้ตอบ NO
#  Sample Case
#  Sample Input	 Sample Output
# 8
# 5
# 8
# 1
# 7
# 4
# 4
# 3

# 8
# 2
# 8
# 10
# NO