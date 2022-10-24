"""[Midterm] Key"""
 
def main(text_id):
    """[Midterm] Key"""
    ans = sum(map(int, text_id)) + int(text_id[-3:])*10
    print("%04d" % (ans%10000 if ans >= 10000 else ans + 1000 if ans < 1000 else ans))
main(input())

# """key"""
# def main():
#     """key"""
#     num = int(input())
#     num5 = 0
#     for i in str(num):
#         num5 += int(i)
#     num2 = (num % 1000)*10
#     ans = num2 + num5
#     if ans >= 10000:
#         print("%04d"%(ans % 10000))
#     elif ans < 1000:
#         print("%04d"%(ans+1000))
#     else:
#         print("%04d"%(ans))
# main()

# จากตัวเลข 13 หลัก ในบัตรประชาชน จงหาค่า Key ซึ่งเป็นตัวเลขสี่หลัก ด้วยวิธีการดังนี้

# 1) หาผลรวมของตัวเลขทั้ง 13 หลัก
# 2) เอาค่า 3 หลักสุดท้าย คูณด้วย 10
# 3) เอาค่าจากข้อ 1) และ 2) มาบวกกัน จะได้เป็น Key ถ้าหากได้ค่ามากกว่าสี่หลักให้ตัดเอาแค่สี่หลักสุดท้าย
# แต่ถ้าค่าน้อยกว่า 1,000 ให้บวก เพิ่ม 1,000 ก็จะได้เลขสี่หลัก ซึ่งเป็น Key

#  Specification
#  Input Specification	 Output Specification

# บรรทัดเดียวคือเลขประจำตัวประชาชน 13 หลัก

# บรรทัดเดียวแสดงค่า Key ของเลขบัตรประจำตัวประชาชนออกมา
#  Sample Case
#  Sample Input	 Sample Output
# 1234567890123
# 1281

# 5146882735998
# 0055