""" Milk V2 """


def milk():
    """ Input then print """
    price = float(input())  # นมขวดละ 10
    lid = int(input())  # จำนวนฝา 2
    lid_exchange = int(input())  # นมที่ได้จากการใช้ฝาเเลก 1
    empty_bottle = int(input())  # ขวดเปล่า 4
    bottle_exchange = int(input())  # นมที่ได้จากการใช้ขวดเปล่าเเลก 1
    money = float(input())  # มีเงิน 100
    total = 0
    money -= price
    while money >= 0:
        total += 1
        if empty_bottle != 0:
            if total % empty_bottle == 0:
                total += bottle_exchange
        print('ขวด', total)
        if lid != 0:
            if total % lid == 0:
                total += lid_exchange
        print('ฝา', total)
        money -= price
    print(total)
milk()

# """[Midterm] Milk V.1"""
# def main():
#     """[Midterm] Milk V.1"""

#     price = int(input())
#     lid = int(input())
#     free = int(input())
#     money = int(input())
#     total = 0

#     money -= price
#     while money >= 0:
#         total += 1
#         if lid != 0:
#             if total % lid == 0:
#                 total += free
#         money -= price
#     print(total)
# main()

# ณ ฟาร์มโคนมแห่งนึงในประเทศวันเดอร์แลนด์ ได้มีการตั้งราคาและโปรโมชันสำหรับการขายนมวัวที่เปลี่ยนไปมาไม่ซ้ำกันในแต่ละวันขึ้นกับความพึงพอใจของเจ้าของฟาร์ม
# ซึ่งนั่นทำให้เจ้าของฟาร์มเองก็มีความสับสนว่าถ้าลูกค้าจ่ายเงินมาเท่านี้ลูกค้าจะได้นมวัวกลับไปกี่ขวดกันแน่? แต่ก็ไม่อยากตั้งราคาที่แน่นอน เพราะความอินดี้ส่วนตัวของเจ้า
# ของฟาร์มและถือเป็นจุดขายของฟาร์ม(?)ด้วย จึงมาขอร้องให้คุณเขียนระบบง่ายๆที่รับราคานมต่อขวด ขวดละ a บาท โดยมีโปรโมชันคือนำฝาขวดทุกๆ b ฝา จะสามารถ
# แลกนมได้ c ขวด และหากลูกค้ามีเงิน d บาทจะได้รับนมสูงสุดกี่ขวด


#  Specification
#  Input Specification	 Output Specification

# 4 บรรทัด เป็นจำนวนเต็ม ประกอบด้วย:
# a {a > 0}
# b {b >= 0}
# c {c >= 0; c < b เมื่อ b != 0}
# d {d >= 0}

# 1 บรรทัด แสดงจำนวนนมขวดทั้งหมดที่ลูกค้าจะได้รับ

#  Sample Case
#  Sample Input	 Sample Output
# 40
# 3
# 1
# 275
# 8

# 200
# 7
# 2
# 1560
# 9
