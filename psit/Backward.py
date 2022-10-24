"""Backward"""

def main():
    """Backward"""
    total = []
    while True:
        txt = input()
        if txt == "NULL":
            break
        total.append(txt) #นำ txt ไปเก็บไว้ใน list  ถ้าปริ้น print(total) = ['ASD', 'ACM', 'ICPC', '12345', 'NULL']
        # if txt == "NULL":
        #     break
    # total = total[:-1:] #ทำให้ NULL หายไป
    total = total[::-1] #สลับตำแหน่ง
    for i in total:
        print(i)
main()
