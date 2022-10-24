"""Saint Seiya"""
def main(sec, num, count1, count2):
    """ฟังก์ชั่น Saint Seiya"""
    if num <= 0:
        print(12*(sec-1))
    else:
        for i in range(2, sec+1, 2):
            if i%6 == 0 and count1 <= num:
                count1 += 1
            elif i%2 == 0 and count1 <= num:
                count1 += 165
            if count1 > num:
                count2 = 12*(sec- i)
                break
            if count1 == num:
                count2 = 12*(sec- i)
                break
        count3 = count2 -12
        if count3 <= 0:
            count3 = 0
        print(count1 + count3)
main(int(input()), int(input()), 0, 0)
