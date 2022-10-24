"""Century"""

def main():
    """ฟังก์ชัน Century"""
    num = int(input())
    for _ in range(num):
        txt_year = input()
        year = int(txt_year[5:])
        if 'B.E.' in txt_year:
            year -= 543
        if year < 0:
            print('ERROR')
        elif year%100 == 0:
            print(year//100)
        else:
            print(year//100+1)
main()
