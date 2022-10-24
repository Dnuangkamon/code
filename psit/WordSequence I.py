""" WordSequence I """
def main():
    """ WordSequence I """
    txt = str(input())
    list_txt = []
    for i in range(len(txt)):
        txt1 = len(txt)-i
        txt2 = txt[:txt1]
        list_txt.append(txt2)
    for j in sorted(list_txt):
        print(j)
main()
