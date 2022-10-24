"""Sequence XII""" #mirror
 
def main():
    """Sequence XII"""
    num = int(input())
    for i in range(-num+1, num):
        i = abs(i)
        for j in range(-num+1, num):
            j = abs(j)
            numnub = num-abs(i-j)
            ans = "%02d"%numnub
            print(ans, end=" ")
        print()
main()

# 05 04 03 02 01 02 03 04 05
# 04 05 04 03 02 03 04 05 04
# 03 04 05 04 03 04 05 04 03
# 02 03 04 05 04 05 04 03 02
# 01 02 03 04 05 04 03 02 01
# 02 03 04 05 04 05 04 03 02
# 03 04 05 04 03 04 05 04 03
# 04 05 04 03 02 03 04 05 04
# 05 04 03 02 01 02 03 04 05