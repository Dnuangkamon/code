""" AlmostMean """
def main():
    """ฟังก์ชั่น AlmostMean """
    number_student = int(input())
    stu_list = []
    score = []
    for _ in range(number_student):
        txt = input()
        stu_list += [txt[:8]]
        score += [float(txt[9:])]
    mean = sum(score)/number_student
    dic = sorted(score)
    count = ''
    for scr in dic:
        if scr > mean:
            break
        count = scr
    rank = stu_list[score.index(count)]
    print('%s\t%s' %(rank, count))
main()
