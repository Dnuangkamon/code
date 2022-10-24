"""Cat Parade"""
def main():
    """Cat Parade"""
    name_list = [] #เก็บชื่อแมวเพื่อนับจำนวน
    cat_list = [] #บอกตำแหน่ง
    p_cat = 0
    while True:
        name_cat = input()
        if name_cat == 'END':
            break
        name_cat = name_cat.split(', ')
        for i in name_cat:
            p_cat += 1
            if i == 'IT\'S A DOG':
                name_list.pop(-1)
                cat_list.pop(-1)
                p_cat -= 2
            else:
                if name_list.count(i) == 0:
                    cat = i + ' ' + str(p_cat) #ใส่ชื่อแมวกับตำแหน่ง
                    cat_list += [cat]
                name_list += [i]
    name_list.sort()
    cat_list.sort()
    for i in cat_list:
        cat_r = str(i).rfind(' ')
        cat_count = name_list.count(i[0:cat_r])
        print(i, cat_count)
main()
