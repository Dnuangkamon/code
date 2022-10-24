"""SqFree"""
def squarefree(numn):
    """ลาก่อน"""
    for i in range(2, round(numn**0.5) + 1):
        if numn % (i**2) == 0:
            return False
    return 1

def main():
    """function"""
    num = int(input())
    if num in range(1, 9999+1):
        ans = 0
        for j in range(1, num+1):
            squarefree(j)
            ans += squarefree(j)
        print(ans)
    if num in range(10000, 19997+1):
        ans = 6083
        for j in range(10000, num+1):
            squarefree(j)
            ans += squarefree(j)
        print(ans)
    if num in range(19998, 39999+1):
        ans = 12159
        for j in range(19998, num+1):
            squarefree(j)
            ans += squarefree(j)
        print(ans)
    if num in range(40000, 50000+1):
        ans = 24310
        for j in range(40000, num+1):
            squarefree(j)
            ans += squarefree(j)
        print(ans)
main()



'''SqFree'''

def main(num):
    '''main'''
    for i in range(2, num+1):
        for j in range(2, int(i**0.5)+1):
            if i%(j**2) == 0:
                num -= 1
                break
    return num
print(main(int(input())))