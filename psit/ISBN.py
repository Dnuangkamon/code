"""ISBN"""

def main(check, summ):
    """ฟังก์ชั่น ISBN"""
    kum_tob = ''
    last_word = int(len(check))
    for i in range(9):
        summ += ((10-i)*int(check[i]))
    if -summ%11 < 10:
        if -summ%11 == int(check[last_word-1]):
            kum_tob += "Yes"
        elif -summ%11 != int(check[last_word-1]):
            kum_tob += "No %d" %(-summ%11)
    else:
        if "X" == check[last_word-1]:
            kum_tob += "Yes"
        elif -summ%11 != int(check[last_word-1]):
            kum_tob += "No X"
    print(kum_tob)
main(input().replace("-", ""), 0)

# """ISBN"""
# def isbn():
#     """ISBN"""
#     data = input()
#     code = data.replace("-", "")
#     x_10 = -((10*int(code[0]))+(9*int(code[1]))+(8*int(code[2]))\
#             +(7*int(code[3]))+(6*int(code[4]))+(5*int(code[5]))+(4*int(code[6]))\
#             +(3*int(code[7]))+(2*int(code[8])))%11
#     if str(x_10) == "10":
#         x_10 = "X"
#     if str(x_10) == code[-1]:
#         print("Yes")
#     else:
#         print("No %s"%(x_10))
# isbn()
