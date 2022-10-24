"""impostar"""

def main(alive, dead, check):
    """ฟังก์ชั่น impostar"""
    while True:
        game = input()
        if game == 'Start':
            break
        game_find = game.find(':')
        alive += [[game[2:game_find-2], game[game_find+3:-2]]]
        alive.sort()
    while True:
        die = input()
        if die == 'End':
            break
        for i in alive:
            if die == i[0]:
                alive.remove(i)
                dead += [i]
        dead.sort()
    for i in alive: #หาจำนวน Impostor ที่ยังอยู่
        if i[1] == 'Impostor':
            check += 1
    print(check, 'Impostor Remains')
    print('***Alive***')
    for i in alive:
        print(*i, sep=(' : '))
    print('***Dead***')
    for i in dead:
        print(*i, sep=(' : '))
main([], [], 0)
