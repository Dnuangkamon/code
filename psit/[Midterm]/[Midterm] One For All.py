"""[Midterm] One For All"""
def main():
    """[Midterm] One For All"""
    number = int(input())
    txt_1 = ''
    for i in range(1, number+1):
        if i%2 == 0 and i != number:
            txt = input()
            txt_1 += txt + "-"*i
        if i%2 != 0 and i != number:
            txt = input()
            txt_1 += txt + "*"*i
        if number == i:
            txt = input()
            txt_1 += txt + "_" + str(number)
    print(txt_1)
main()

# 5
# Allmight
# Izuku
# Shoto
# Denki
# Bakugo

# Allmight*Izuku--Shoto***Denki----Bakugo_5