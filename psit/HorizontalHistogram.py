""" HorizontalHistogram """

def main():
    """ฟังก์ชั่น HorizontalHistogram """
    keep = list()
    keep.extend(input())
    list_keep = list(set(keep))
    list_keep.sort(key=lambda x: x.swapcase())
    for i in list_keep:
        count = keep.count(i)
        if count%5 == 0:
            poo = i + ' : ' + (count//5)*'-----|' + (count%5)*'-'
            print(poo[0:-1])
        else:
            poo = i + ' : ' + (count//5)*'-----|' + (count%5)*'-'
            print(poo)
main()
