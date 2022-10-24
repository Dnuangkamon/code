""" Pro """
def pro():
    """ ฟังก์ชั่น Pro """
    num_x = int(input())
    num_y = int(input())
    num_a = int(input())
    num_z = int(input())
    price = (num_z//num_x)*num_y*num_a
    price += (num_z%num_x)*num_a #เศษคนที่ไม่ได้แถม
    print(price)
pro()
