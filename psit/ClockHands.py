"""ClockHands"""
def main(clock, minute):
    """main"""
    if (clock == 0 and minute == 0) or (minute < clock*5+(minute/12) % 60 < minute+1):
        print("True")
    else:
        print("False")
main(int(input()), int(input()))
