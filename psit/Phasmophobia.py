'''Phasmophobia'''

def main(type1, type2, type3):
    '''main'''
    ghost = {
        'EMF Level 5' : {'Banshee', 'Jinn', 'Oni', 'Phantom', 'Revenant', 'Shade'},
        'Ghost Writing' : {'Demon', 'Oni', 'Revenant', 'Shade', 'Spirit', 'Yurei'},
        'Fingerprints' : {'Banshee', 'Poltergeist', 'Revenant', 'Spirit', 'Wraith'},
        'Spirit Box' : {'Demon', 'Jinn', 'Mare', 'Oni', 'Poltergeist', 'Spirit', 'Wraith'},
        'Freezing Temperatures': {'Banshee', 'Demon', 'Mare', 'Phantom', 'Wraith', 'Yurei'},
        'Ghost Orb' : {'Jinn', 'Mare', 'Phantom', 'Poltergeist', 'Shade', 'Yurei'},
        'No evidence' : {'Banshee', 'Jinn', 'Oni', 'Phantom', 'Revenant', 'Shade', 'Spirit', \
            'Wraith', 'Yurei', 'Poltergeist', 'Demon', 'Mare'}}
    result = set.intersection(ghost[type1], ghost[type2], ghost[type3])
    if result == set():
        print('Not yet discovered')
    else:
        result = sorted(list(result))
        print(*result, sep='\n')
main(input(), input(), input())

""" Phasmophobia """
def main():
    """function1"""
    txt1, txt2, txt3 = input(), input(), input()
    txt_list = []
    ans = ''
    txt_list.append(txt1)
    txt_list.append(txt2)
    txt_list.append(txt3)
    ghost1 = txt_list.count('EMF Level 5')
    ghost2 = txt_list.count('Ghost Writing')
    ghost3 = txt_list.count('Fingerprints')
    ghost4 = txt_list.count('Spirit Box')
    ghost5 = txt_list.count('Freezing Temperatures')
    ghost6 = txt_list.count('Ghost Orb')
    notghost = txt_list.count('No evidence')
    if (ghost1 + ghost3 + ghost5 + notghost) > 2:
        ans += 'Banshee '
    if (ghost2 + ghost4 + ghost5 + notghost) > 2:
        ans += 'Demon '
    if (ghost1 + ghost4 + ghost6 + notghost) > 2:
        ans += 'Jinn '
    if (ghost4 + ghost5 + ghost6 + notghost) > 2:
        ans += 'Mare '
    if (ghost1 + ghost2 + ghost4 + notghost) > 2:
        ans += 'Oni '
    if (ghost1 + ghost5 + ghost6 + notghost) > 2:
        ans += 'Phantom '
    if (ghost3 + ghost4 + ghost6 + notghost) > 2:
        ans += 'Poltergeist '
    if (ghost1 + ghost2 + ghost3 + notghost) > 2:
        ans += 'Revenant '
    if (ghost1 + ghost2 + ghost6 + notghost) > 2:
        ans += 'Shade '
    if (ghost2 + ghost3 + ghost4 + notghost) > 2:
        ans += 'Spirit '
    if (ghost3 + ghost4 + ghost5 + notghost) > 2:
        ans += 'Wraith '
    if (ghost2 + ghost5 + ghost6 + notghost) > 2:
        ans += 'Yurei '
    ans = ans.split()
    ans.sort()
    return ans

def main2(ans):
    """function2"""
    if ans != []:
        print(*ans, sep='\n')
    else:
        print('Not yet discovered')
main2(main())