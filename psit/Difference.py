"""Difference"""
import json
def main(lista, listb, mydict):
    """Difference"""
    checkall = set(lista).union(set(listb))
    for i in checkall:
        if abs(listb.count(i) - lista.count(i)) != 0:
            mydict[i] = abs(listb.count(i) - lista.count(i))
    if mydict != dict():
        for i in sorted(mydict):
            print(i, mydict[i])
    else:
        print("ONAJI DAYO!")
main(json.loads(input()), json.loads(input()), dict())