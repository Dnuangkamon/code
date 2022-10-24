"""Antenna"""
import json
def main(numr, point, count):
    """Antenna"""
    point.sort()
    pointcheck = point.copy()
    while pointcheck != []:
        check = min(pointcheck) + (numr*2)
        count += 1
        for i in point:
            if i in pointcheck and i <= check:
                pointcheck.remove(i)
    print(count)
main(float(input()), json.loads(input()), 0)
