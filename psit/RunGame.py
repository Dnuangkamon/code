"""RunGame"""
def rungame():
    """ฟังก์ชั่น RunGame"""
    number = input().split()
    start = 0
    ans = 0
    for i in number:
        ans += abs(start - int(i))
        start = int(i)
    print(ans)
rungame()
