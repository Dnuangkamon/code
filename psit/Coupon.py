""" Coupon """

def pro():
    """ ฟังก์ชั่น Coupon """
    cost = float(input())
    cost_1, cost_2 = cost, cost
    discount1 = input().split()
    num_a, num_b = float(discount1[0]), float(discount1[1])
    discount2 = input().split()
    num_x, num_y = float(discount2[0]), float(discount2[1])
    if cost >= num_b:
        cost_1 = cost - num_a
    if cost >= num_y:
        cost_2 = cost*(100-num_x)/100
    if cost_1 < cost_2:
        print('1 %.1f' %cost_1)
    elif cost_1 > cost_2:
        print('2 %.1f' %cost_2)
    elif cost_1 == cost_2 == cost:
        print('Nope')
    elif cost_1 == cost_2:
        if num_b > num_y:
            print('2 %.1f' %cost_2)
        else:
            print('1 %.1f' %cost_1)
pro()
