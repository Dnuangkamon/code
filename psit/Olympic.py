"""Olympic"""

def coin_1(coin):
    """Olympic เรียงเหรียญ"""
    return int(coin[1])*-1, int(coin[2])*-1, int(coin[3])*-1, coin[0]

def main(number):
    """ฟังก์ชั่น Olympic"""
    keep = []
    for _ in range(number):
        keep += [tuple(input().split())]
    keep.sort(key=coin_1)
    count = 0
    gold1, silver1, bronze1, space1 = -1, -1, -1, ''
    for i in keep:
        count += 1
        count1 = count
        gold, silver, bronze = int(i[1]), int(i[2]), int(i[3])
        if gold == gold1 and silver == silver1 and bronze == bronze1:
            count1 = space1
        total = gold + silver + bronze
        print(count1, " ".join(i), total)
        gold1, silver1, bronze1, space1 = gold, silver, bronze, count1
main(int(input()))
