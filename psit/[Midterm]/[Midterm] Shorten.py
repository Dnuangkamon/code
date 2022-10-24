"""[Midterm] Shorten"""
 
def main():
    """[Midterm] Shorten"""
    state = 'start'
    prev = None
    txt_1 = ''
    while True:
        num = int(input())
        if state == 'start' and num == -1:
            break
        elif state == 'wait' and num == -1:
            txt_1 += '-'+ str(prev)
            break
        elif state == 'start' and prev == None:
            txt_1 += str(num)
        elif state == 'start' and num-prev == 1:
            state = 'wait'
        elif state == 'start' and num-prev != 1:
            txt_1 += ', ' + str(num)
        elif state == 'wait' and num-prev != 1:
            txt_1 += '-' + str(prev) + ', ' + str(num)
            state = 'start'
        prev = num
    print(txt_1)
main()

# ให้รับตัวเลขจำนวนเต็มบวกเข้ามาเรื่อยๆทีละบรรทัด จนกระทั่งได้รับตัวเลข -1 จึงหยุด โดยตัวเลขที่รับเข้ามา จะมีค่าเพิ่มขึ้นเรื่อยๆเสมอ

# และให้ย่อตัวเลขที่รับมาเหล่านั้นให้สั้นลงโดยใช้เครื่องหมาย - 

# เช่น สมมุติว่ารับค่าเข้ามาเป็น

# 1
# 2
# 3
# 5
# 7
# 9
# 10
# -1

# ให้เขียนย่อเป็น 1-3, 5, 7, 9-10
 
#  Specification
#  Input Specification	 Output Specification

# จำนวนบรรทัดไม่แน่นอน แต่เป็นตัวเลขจำนวนเต็มบวก เรียงจากน้อยไปมากในแต่ละบรรทัด

# มี 1 บรรทัด เป็นการเขียนแบบย่อ ตามรูปแบบที่กำหนด
#  Sample Case
#  Sample Input	 Sample Output
# 1
# 2
# 3
# 5
# 7
# 9
# 10
# -1
# 1-3, 5, 7, 9-10
# 1
# 2
# 3
# 4
# 5
# -1
# 1-5