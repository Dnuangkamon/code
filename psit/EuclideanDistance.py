"""EuclideanDistance"""
def main(num, mylist, phase):
    """EuclideanDistance"""
    for _ in range(num):
        dot = input().split()
        mylist.append(dot)
    for i in range(len(mylist)-1):
        phase += ((int(mylist[i][0])-int(mylist[i+1][0]))**2 +\
        (int(mylist[i][1])-int(mylist[i+1][1]))**2)**0.5
    print("%.2f"%phase)
main(int(input()), [], 0)

'''EuclideanDistance'''

def distance(point_1, point_2):
    '''function find distance'''
    return ((point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2)**0.5

def main():
    '''function main'''
    list_point = [list(map(int, input().split())) for _ in range(int(input()))]
    dist = 0
    for i in range(len(list_point) - 1):
        dist += distance(list_point[i], list_point[i+1])
    print('%.2f'%dist)
main()