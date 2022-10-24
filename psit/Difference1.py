"""Difference"""

def main():
    """ฟังก์ชั่น Difference"""
    list_a = input()
    list_b = input()
    check = set(list_a).difference((set(list_b)))
    print(check)
main()
