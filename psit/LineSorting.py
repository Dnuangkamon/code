""" LineSorting """

def main():
    """ ฟังก์ชั่น LineSorting"""
    num = int(input())
    txt1 = []
    for _ in range(num):
        txt = input()
        txt1.append(txt)
    print(*(sorted(txt1, key=len)), sep="\n")
main()
