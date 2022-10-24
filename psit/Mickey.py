""" Mickey """
def mickey1():
    """ ฟังก์ชั่น Mickey """
    mickey_home = int(input())
    list_mickey = []
    list_home = []
    list_max = []
    for _ in range(mickey_home):
        mickey = int(input())
        list_mickey.append(mickey)
    for _ in range(mickey_home):
        home = int(input())
        list_home.append(home)
    list_mickey.sort()
    list_home.sort()
    for i in range(mickey_home):
        maxx = (abs(int(list_mickey[i])-int(list_home[i])))
        list_max.append(maxx)
    print(max(list_max))
mickey1()
