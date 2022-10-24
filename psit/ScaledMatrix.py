"""ScaledMatrix"""
def main(num_i, num_j):
    """ScaledMatrix"""
    ans, ans2, ans3, anss = [], [], [], ""
    for _ in range(num_j*num_i):
        data = float(input())
        ans.append(data)
    fix = min(ans)
    for i in ans:
        ans2.append(i+abs(fix))
    fix2 = max(ans2)
    for i in ans2:
        ans3.append(i/fix2)
    for i in ans3:
        i = "%.2f"%i
        anss += str(i)+" "
        if anss.count(" ")%num_j == 0:
            print(anss)
            anss = ""
main(int(input()), int(input()))
