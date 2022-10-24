"""CaesarV1"""
def main(number, txt):
    """ฟังก์ชั่น CaesarV1"""
    for i in txt:
        count = 0
        if not i.isidentifier() or i.isnumeric():
            count = 1
        elif i.islower():
            i = ord(i) + number
            i = i-26*(i > 122) + 26*(i < 97)
        else:
            i = ord(i) + number
            i = i-26*(i > 90) + 26*(i < 65)
        if count != 0:
            print(i, end='')
        elif count == 0:
            print(chr(i), end='')
main(int(input())%26, input())
