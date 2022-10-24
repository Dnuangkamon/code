"""Ball"""
def main(numh, ans):
    """Ball"""
    import math
    check = numh
    while math.floor(check) > 0:
        check *= 0.6
        ans += 1
    print(ans-1)
main(float(input())*100, 0)
