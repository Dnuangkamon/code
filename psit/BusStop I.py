"""Bus Stop"""
def main():
    """ฟังก์ชั่น Bus Stop"""
    valence, tablet = int(input()), int(input())
    ans, station = 0, 0
    list_bus, data = [], []
    while station != tablet:
        bus = input().split()
        bus[0] = int(bus[0])
        station += 1
        data.append(bus)
    data.sort()
    for i in range(1, tablet+1):
        ans += list_bus.count(i)
        while i in list_bus:
            list_bus.remove(i)
        data[i-1].pop(0)
        for j in data[i-1]:
            if len(list_bus) == valence:
                break
            if i < int(j) <= tablet:
                list_bus.append(int(j))
    print(ans)
main()
