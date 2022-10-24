"""Perfect"""
def main():
    """อย่าดิ"""
    num = int(input())
    ans = 0
    if num < 496:
        ans += 34
    elif num <= 7127 + 1000:
        ans += (496+34)
    elif num < 33550336:
        ans += (7127 + 34 + 1 + 1000)
        ans += 496
    elif num <= 7570769055+9000000-1+1000000000+10100000:
        ans += (33550336+34)
        ans += (7127+496+1001)
    elif num < 137437691327+1000001:
        ans += (7570769055+1010100000+9000000+496+34)
        ans += (1+33550336+7127+1001)
    else:
        ans += (137437691327+1000001+7570769055+1010100000+7127+1001+496+34)
        ans += (9000000+33550336)
    print(ans)
main()


'''Perfect'''
def mian(num):
    '''mian'''
    total = 0
    ans = 0
    for i in range(2, num+1):
        for j in range(1, int(i**0.5)+1):
            if i%j == 0:
                total += j
                if j > 1 and j != i/j:
                    total += i/j
        if total == i:
            ans += i
        total = 0
    return ans
print(mian(int(input())))