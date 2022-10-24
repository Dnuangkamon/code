"""Scout"""
def main(num, total, ans):
    """Scout"""
    for _ in range(num):
        npq = input().split()
        wegg = input().split()
        for i in range(len(wegg)):
            wegg[i] = float(wegg[i])
        wegg.sort()
        numn, nump, numq = int(npq[0]), int(npq[1]), int(npq[2])
        for i in range(min(numn, nump)):
            total += int(wegg[i])
            if total > numq:
                break
            else:
                ans += 1
        print(ans)
        total, ans = 0, 0
main(int(input()), 0, 0)
