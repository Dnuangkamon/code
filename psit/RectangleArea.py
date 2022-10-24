"""RectangleArea"""
def main(dataa, datab, ans):
    """RectangleArea"""
    dot1a, dot1b = [int(dataa[0]), int(dataa[1])], [int(datab[0]), int(datab[1])]
    dot2a = [int(dataa[0])+int(dataa[2]), int(dataa[1])+int(dataa[3])]
    dot2b = [int(datab[0])+int(datab[2]), int(datab[1])+int(datab[3])]
    distx = (min(dot2a[0], dot2b[0]) - max(dot1a[0], dot1b[0]))
    disty = (min(dot2a[1], dot2b[1]) - max(dot1a[1], dot1b[1]))
    if distx > 0 and disty > 0:
        ans = distx * disty
    if ans == 0:
        print("no overlapping")
    else:
        print(ans)
main(input().split(), input().split(), 0)
