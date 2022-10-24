"""Music Lover"""
def music():
    """Music Lover"""
    number = int(input())
    list_music = []
    list_music1 = []
    set_music = set()
    for _ in range(number):
        music_s = input().split('-')
        list_music.append(music_s[0])
        list_music.append(music_s[1])
    for i in set(list_music):
        print(i)
        for j in list_music1:
            print(j)
music()
