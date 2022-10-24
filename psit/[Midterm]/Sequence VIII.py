"""Sequence VIII"""

def main():
    """Sequence VIII"""
    num = int(input())
    for i in range(num):
        # + - ใช้ 2 ตัวแปร x, num
        print("   "*(num-i-1), end="")
        for number in range(i + 1):
            print("%02d" % (number+1), end=" ")
        print()


main()

#             01
#          01 02
#       01 02 03
#    01 02 03 04
# 01 02 03 04 05
