'''Tax'''

def tax(num1, num2):
    '''ฟังก์ชั่น Tax'''
    cost = 0
    if num2 >= 1801:
        cost += (num2-1800)*4
        num2 -= (num2 - 1800)
    if num2 >= 601:
        cost += (num2-600)*1.5
        num2 -= (num2-600)
    cost += num2*0.5
    if num1 > 5:
        if num1 >= 10:
            cost = cost*50/100
        else:
            discount = {6:90, 7:80, 8:70, 9:60}
            cost = cost*discount[num1]/100
    print('%.2f' %cost)
tax(int(input()), int(input()))
