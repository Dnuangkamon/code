"""Guess"""
def main(ans, ans2, maax, miin, ree):
    """Guess"""
    while 1:
        txtt = input()
        txt = txtt.split()
        if txtt == "END":
            break
        if txt[2] == "YES" and txt[0] == "=":
            ans.append(int(txt[1]))
        elif txt[2] == "YES" and txt[0] == ">":
            maax.append(int(txt[1]))
        elif txt[2] == "YES" and txt[0] == "<":
            miin.append(int(txt[1]))
        elif txt[2] == "NO" and txt[0] == "=":
            ree.append(int(txt[1]))
        elif txt[2] == "NO" and txt[0] == ">": #<=
            miin.append(int(txt[1])+1)
        elif txt[2] == "NO" and txt[0] == "<": #>=
            maax.append(int(txt[1])-1)
    num1, num2 = 0, 101
    if maax != []:
        num1 = max(maax)+1
    if miin != []:
        num2 = min(miin)
    for i in range(num1, num2):
        ans2.append(i)
    final = sorted((set(ans)-set(ree).union((set(ans) - set(ans2)))))
    if ans == []:
        final = sorted((set(ans2)-set(ree)))
    print(*final)
main([], [], [], [], [])
