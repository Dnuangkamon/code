"""Kayak"""
def main(num, weight, mylist):
    """Kayak"""
    weight = [int(i) for i in weight]
    weight.sort()
    for _ in range(num-1):
        mylist2 = []
        for i in range(len(weight)-1):
            final = int(weight[i+1])-int(weight[i])
            mylist2.append(final)
        final = mylist2.index(min(mylist2))
        weight.pop(final)
        weight.pop(final)
        mylist.append(min(mylist2))
    print(sum(mylist))
main(int(input()), input().split(), [])
