""" Roman """

def main():
    """ ฟังก์ชั่น Roman """
    txt = str(input())
    check = 0
    list_roman = ["IV", "IX", "XL", "XC", "CD", "CM"]
    list_number = [4, 9, 40, 90, 400, 900]
    for j in range(len(list_roman)):
        if txt.count(list_roman[j]) == 1:
            text = txt.replace(list_roman[j], "")
            check += list_number[j]
            txt = text
    for i in txt:
        if i == 'I' or i == 'V' or i == 'X' or i == 'L' or i == 'C' or i == 'D' or i == 'M':
            number = i.replace('I', '1').replace('V', '5').replace('X', '10')\
                .replace('L', '50')\
                    .replace('C', '100').replace('D', '500').replace('M', '1000')
            check += int(number)
    print(int(check))
main()
