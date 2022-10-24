""" Duplicate I """
def main():
    """ Duplicate I """
    number_m = int(input())
    number_n = int(input())
    list_m = []
    list_n = []
    ans = []
    for _ in range(number_m):
        list_m.append(int(input()))
    for _ in range(number_n):
        list_n.append(int(input()))
    for i in range(number_m):
        num = list_n.count(list_m[i])
        if num != 0:
            ans.append(list_m[i])
    if len(ans) == 0:
        print("Nope")
    else:
        ans.sort(reverse=True)
        for i in ans:
            print(i, end=' ')
            print()
main()
