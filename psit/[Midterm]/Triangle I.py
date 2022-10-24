"""Triangle I"""
def main():
    """Triangle I"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    sol = ((num1**2)+(num2**2))-num3**2 <= 0.01
    sol_1 = ((num3**2)+(num2**2))-num1**2 <= 0.01
    sol_2 = ((num1**2)+(num3**2))-num2**2 <= 0.01
    if sol or sol_1 or sol_2:
        print('Yes')
    else:
        print('No')
main()

# ฉันมีความคิดที่จะสร้างรูปสามเหลี่ยมมุมฉากขึ้นมาด้วยแท่งไม้เป็นพร็อพสำหรับถ่ายรูปสักหน่อย
# และพอดีว่าฉันอยากได้เยอะๆ เลยกดสั่งเยอะไปหน่อย จึงได้ไม้มาเยอะมาก

# แต่ฉันไม่รู้ว่าแท่งไม้สามอันที่จะเอามาสร้างรูปสามเหลี่ยมมุมฉากนั้น
# จะสามารถสร้างได้จริงๆมั้ย โดยที่รูปสามเหลี่ยมมุมฉากที่ขึ้นมา จะต้องเป็นรูปแบบปิด
# คือใช้ไม้ปิดเป็นรูปสามเหลี่ยมได้พอดี ไม่เกินออกมาให้คนเดินเตะ
# จึงอยากให้คุณเขียนโปรแกรมขึ้นมาตรวจสอบหน่อย

# ฉันจะมีความยาวของไม้ทั้งสามแท่งมาให้
# คนส่งไม้เค้าแปะ Tag ความที่ตัวไม้ด้วย เป็นเซนติเมตร ฉันเลยไม่ต้องวัดเอง

#  Input Specification	 Output Specification

# 3 บรรทัด เป็นความยาวของไม้ทั้งสามแท่ง (float)

# 1 บรรทัด
# Yes ถ้าสามารถสร้างได้
# No ถ้าสร้างไม่ได้

# ความแตกต่างระหว่างด้านตรงข้ามมุมฉากกำลังสอง กับผลรวมของด้านประกอบมุมฉากกำลังสอง
# ถ้าหากมีความแตกต่าง ไม่เกิน 0.01 ถือว่าสร้างได้
#  Sample Case
#  Sample Input	 Sample Output
# 3
# 4
# 5
# Yes
# 10
# 12
# 14
# No