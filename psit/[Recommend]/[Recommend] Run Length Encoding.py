"""Run Length Encoding"""
def main(txt, list_1, ans):
    """Run Length Encoding"""
    last = txt[0]
    for i in txt:
        if last != i:
            list_1.append(ans)
            last, ans = i, i
        else:
            ans += i
    for j in range(len(list_1)):
        print(str(len(list_1[j])) + list_1[j][0], end='')
main(input() + '.', [], '')

# """Run Length Encoding"""
# def main():
#     """Run Length Encoding"""
#     text = input()
#     word = text[0]
#     ans = 0
#     for i in text:
#         if i == word:
#             ans += 1
#         elif i != word:
#             print(str(ans)+word, end="")
#             word = i
#             ans = 0
#             ans += 1
#     print(str(ans)+word, end="")
# main()

# Run-length Encoding เป็นการเข้ารหัสโดยรวมข้อมูลที่อยู่ใกล้เคียงกัน ที่เหมือนกัน ไว้ด้วยกัน เพื่อลดขนาดของข้อมูล (แม้ว่าบางทีมันอาจจะเพิ่มก็ได้)
# ตัวอย่าง
# aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa
# จะสังเกตว่า ข้างหน้า มี a ติดกันอยู่ 5 ตัว ก็จะรวมกันเป็น 5a
# จากนั้น มี h ติดกันอยู่ 6 ตัว ก็จะรวมกันเป็น 6h
# ต่อมา มี m ติดกันอยู่ 7 ตัว ก็จะรวมกันเป็น 7m
# ต่อมา มี u ติดกันอยู่เพียงแค่ตัวเดียว เพราะฉะนั้น จะเก็บข้อมูลเป็น 1u
# ...
# โดยเมื่อเข้ารหัสเสร็จแล้ว ก็จะกลายเป็น 5a6h7m1u7i6a
# จะสังเกตได้ว่า เมื่อเข้ารหัสเสร็จแล้ว จะใช้พื้นที่ในการเก็บข้อมูลน้อยกว่าต้นฉบับนั่นเอง

#  Specification
#  Input Specification	 Output Specification

# String ยาวๆ 1 บรรทัด ความยาวไม่เกิน 255 ตัวอักษร

# String ที่เข้ารหัสแล้ว
#  Sample Case
#  Sample Input	 Sample Output
# aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa
# 5a6h7m1u7i6a