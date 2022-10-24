""" T-Score """
def score():
    """ ฟังก์ชั่น T-Score """
    num_stu = int(input())
    _ = int(input())
    ans = 0
    ans_power2 = 0
    list_score = []
    for _ in range(num_stu):
        score_stu = int(input())
        ans += score_stu #รวมผลบวกทั้งหมด
        ans_power2 += (score_stu**2) #รวมผลบวกทั้งหมด(**2)
        list_score.append(score_stu)
    sum_sd = (((num_stu*(ans_power2))-(ans**2))/(num_stu*(num_stu-1)))**0.5 #หา sd
    sum_x = ans/num_stu #หา x'
    for i in list_score:
        sum_z = (int(i)-sum_x)/sum_sd
        print('%.2f' %(50 + 10*(sum_z)))
score()
