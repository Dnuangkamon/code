"""[Midterm] Bill"""
def main():
    """[Midterm] Bill"""
    money = int(input())
    if money*0.1 < 50:
        money += 50
    elif money*0.1 > 1000:
        money += 1000
    else:
        money += money*0.1
    money += money*0.07
    print("%.2f"%money)
main()

# '''Bill'''
# def main():
#     '''Docstring'''
#     price = int(input())
#     service = 0.1*price
#     if service > 1000:
#         service = 1000
#     elif service < 50:
#         service = 50
#     priceserv = price + service
#     priceall = 0.07*(priceserv) + priceserv
#     print('%.2f'%priceall)
# main()

# ร้านอาหารแห่งหนึ่ง กำหนดค่าบริการไว้ 10% ของราคาอาหารและเครื่องดื่มที่ลูกค้าได้สั่งไป แต่ร้านนี้ได้มีข้อกำหนดว่าค่าบริการจะคิดอย่างน้อย 50 บาท 
# แต่จะไม่เกิน 1000 บาทด้วย ร้านนี้ยังมีการคิด VAT อีก 7% จากราคาที่ได้รวมค่าอาหาร เครื่องดื่ม และค่าบริการแล้ว จงคำนวนหาจำนวนเงินที่ลูกค้าต้อง
# จ่ายหลังจากรวมค่าบริการและ VAT เรียบร้อยแล้ว 
# by นายเชาว์วัฒน์ ยาทองชุน

#  Input Specification	 Output Specification

# 1 บรรทัด เป็นเลขจำนวนเต็มที่แสดงจำนวนเงินรวมเฉพาะค่าอาหารและเครื่องดื่มที่ลูกค้าได้สั่งไป

# 1 บรรทัด เป็นจำนวนจริง ที่เป็นผลรวมที่ลูกค้าต้องชำระเงินหลังจากได้รวมค่าบริการและ VAT 7% เรียบร้อยแล้ว (ให้แสดงเป็นทศนิยม 2 หลัก)
#  Sample Case
#  Sample Input	 Sample Output
# 100
# 160.50

# 1888
# 2222.18

# 99999
# 108068.93