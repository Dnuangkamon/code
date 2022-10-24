""" Day2011 """

def main(day, month):
    """ ฟังก์ชั่น Day2011 """
    week = dict()
    week[0] = "Friday"
    week[1] = "Saturday"
    week[2] = "Sunday"
    week[3] = "Monday"
    week[4] = "Tuesday"
    week[5] = "Wednesday"
    week[6] = "Thursday"
    if month == 1 or month == 10:               #15 Saturday
        mod = (day%7)
    if month == 2 or month == 3 or month == 11: #15 Tuesday
        mod = ((day+3)%7)
    if month == 4 or month == 7:                #15 Friday
        mod = ((day+6)%7)
    if month == 5:                              #15 Sunday
        mod = ((day+8)%7)
    if month == 6:                              #15 Wednesday
        mod = ((day+11)%7)
    if month == 8:                              #15 Monday
        mod = ((day+9)%7)
    if month == 9 or month == 12:               #15 Thursday
        mod = ((day+12)%7)
    print(week[mod])
main(int(input()), int(input()))

# """ Day2011 """
# def main(num_day, month):
#     """ Day2011 """
#     year = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334] #+เเต่ล่ะเดือน ได้ตำแหน่ง num_day
#     week = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"] #ตำแหน่งวัน
#     if month == 1:
#         ans = num_day
#     else:
#         ans = num_day+year[month-2]
#     print(week[ans%7])
# main(int(input()), int(input()))
