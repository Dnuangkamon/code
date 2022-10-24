""" WPM """

def wpm():
    """ ฟังก์ชั่น WPM """
    txt1 = input()
    txt2 = int(input())
    if txt1 == 'Kids':
        if txt2 > 40:
            txt2 = 41
        if txt2 < 11:
            txt2 = 10
        dict_wpm = {
            0:'Very Slow',
            1:'Slow',
            2:'Average',
            3:'Fast',
            4:'Very Fast'
            }
        txt2 -= 1
        print(dict_wpm[txt2//10])
    else:
        if 65 < txt2 < 81:
            print('Very Fast')
        elif txt2 > 80:
            print('Insane')
        else:
            if txt2 < 26:
                txt2 = 25
            dict_wpm = {
                1:'Very Slow',
                2:'Slow/Beginner',
                3:'Intermediate/Average',
                4:'Fast/Advanced',
                5:'Fast/Advanced'
                }
            txt2 -= 6
            print(dict_wpm[txt2//10])
wpm()
