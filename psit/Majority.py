""" Majority """
def main(_, vote, most_vote, most_fre, list_score):
    """ ฟังก์ชั่น Majority """
    for _ in range(vote):
        each_vote = int(input())
        list_score.append(each_vote)
        if list_score.count(each_vote) > most_fre:
            most_fre = list_score.count(each_vote)
            most_vote = each_vote
    if most_fre > (vote/2):
        print(most_vote, most_fre)
    else:
        print('0', most_fre)
main(int(input()), int(input()), '', 0, [])
