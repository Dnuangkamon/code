"""Sort"""
def main(mylist):
    """ฟังก์ชั่น Sort"""
    while True:
        number = input()
        if number == "END":
            break
        mylist.append(int(number))
    for _ in range(len(mylist)):
        for i in range(len(mylist)-1):
            if mylist[i] > mylist[i+1]:
                check = mylist[i]
                mylist[i] = mylist[i+1]
                mylist[i+1] = check
    for j in mylist:
        print(j)
main([])
