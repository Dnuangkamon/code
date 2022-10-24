"""CuteCat CuteFox"""
def main(dic, total_cat, total_fox):
    """ฟังก์ชั่น CuteCat CuteFox"""
    for _ in range(int(input())):
        txt = input()[2:-2].split(' : ')
        dic.update({txt[0][:-1]:txt[1][1:]})
    if 'Garfield' not in dic and 'Cat01' not in list(dic.values()):
        dic.update({'Garfield' : 'Cat01'})
    if 'Fubuki' not in dic and 'Fox01' not in list(dic.values()):
        dic.update({'Fubuki' : 'Fox01'})
    for i in list(dic.values()):
        if 'Cat' in i:
            total_cat += 1
        if 'Fox' in i:
            total_fox += 1
    print('Cat : %d' %(total_cat))
    print('Fox : %d' %(total_fox))
    dic = sorted(sorted(dic.items(), key=lambda x: int(x[1][3:])), key=lambda x: x[1][0])
    for j in dic:
        print(j[0]+' : '+j[1])
main({}, 0, 0)
