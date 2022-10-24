"""BookWorm"""
def main(mylist, ans, ans2):
    """ฟังก์ชั่น BookWorm"""
    for _ in range(int(input())):
        read = float(input())
        for _ in range(int(input())):
            mylist.append(float(input()))
        for i in sorted(mylist):
            ans2 += i
            if ans2 <= read:
                ans += 1
        print(ans)
        mylist, ans, ans2 = [], 0, 0
main([], 0, 0)
