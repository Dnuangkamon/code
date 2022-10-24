"""VerticalHistogram"""

def main():
    """ฟังก์ชั่น VerticalHistogram"""
    keep = list()
    keep.extend(input())
    list_keep = list(set(keep))
    list_keep.sort(key=lambda x: x.swapcase())
    list_count = []
    for i in list_keep:
        count = keep.count(i)
        list_count.append(count)
    for j in range(max(list_count), 0, -1):
        list_k = ''
        for k in list_count:
            if k >= j:
                list_k += '* '
            else:
                list_k += '  '
        print('%03d' %j, list_k)
    print('   ', *list_keep, sep=' ')
main()
