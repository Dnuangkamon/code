"""GasStations"""
def main():
    """เขียนใหม่ด่วน"""
    numc = float(input())
    numx = float(input())
    nump = int(input())
    mylist = []
    fix = 0
    mylist2 = []
    for i in range(nump):
        num = float(input())
        nnn = num - fix
        if nnn > numx or ((numx*nump) < numc):
            mylist = [8888888888]
            break
        else:
            mylist.append(nnn)
            mylist2.append(num)
            fix = num
    ans = 0
    anss = 0
    phase = numc
    count = 0
    if mylist != [8888888888]:
        for i in range(len(mylist)):
            count += mylist[i]
            if ans < numx and phase != 0:
                ans += mylist[i]
            elif ans == numx and phase != 0:
                anss += 1
                phase -= ans
                ans = 0
                ans += mylist[i]
            elif ans > numx and phase != 0:
                anss += 1
                phase -= ans
                ans = 0
                ans += mylist[i-1]
                ans += mylist[i]
    if ans >= numx and phase != 0:
        anss += 1
        phase -= ans
    if count + numx >= numc and mylist != [8888888888]:
        print(anss)
    else:
        print("depleted")
main()

"""GasStations"""
def main(goal, status, all_gas, count):
    """GasStations"""
    remain = status
    if len(all_gas) != 0:
        all_gas += [all_gas[-1]]
    for i in range(len(all_gas) - 1):
        if all_gas[i] > remain:
            break
        elif (all_gas[i] < remain and all_gas[i + 1] <= remain) or all_gas[i] >= goal:
            pass
        else:
            count += 1
            remain = all_gas[i] + status
    print("depleted" if remain < goal else count)
main(float(input()), float(input()), [float(input()) for _ in range(int(input()))], 0)
