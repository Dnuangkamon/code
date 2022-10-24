"""Diamond I"""

def main():
    """Diamond I"""
    for_i = int(input())
    for_j = int(input())
    list_di = []
    ans = 0
    listans = []
    for i in range(for_i):
        dimond = input().split()
        list_di.append(dimond) #listทั้งหมดที่ได้จาก dimond
    for j in range(for_j):
        for i in range(for_i):
            ans += int(list_di[i][j]) #รวมค่าเป็นแนวตั้ง
        listans.append(ans)
        ans = 0 #รีเซ็ตค่า ans ไม่งั้นค่าจะบวกกันหมด
    print(max(listans))
main()
