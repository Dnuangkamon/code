"""SceneSwitch I"""
def main():
    """ยากกกกกกกกกกกกกกกกกก"""
    ans2 = 0
    fix = 0
    txt = ""
    while 1:
        sec = input()
        if sec == "End":
            break
        if float(sec) - fix <= 6 and txt == "":
            fix = float(sec)
            txt += "Day"
        elif float(sec) - fix <= 6 and txt == "Day":
            fix = float(sec)
            txt += "off"
        elif float(sec) - fix <= 6 and txt == "Dayoff":
            fix = float(sec)
            ans2 += 1
            txt = ""
        else:
            txt = "Day"
    print(ans2)
main()
