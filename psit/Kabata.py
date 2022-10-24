"""Kabata"""
def main():
    """ฟังก์ชั่น Kabata"""
    for _ in range(int(input())):
        kabata = input()
        kabata1 = kabata.replace("bakka", "").replace("ba", "").replace("ta", "").replace("ka", "")
        if kabata1 == "" and kabata.find("baka") == -1:
            print("yes")
        else:
            print("no")
main()
