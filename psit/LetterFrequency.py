"""LetterFrequency"""
def main():
    """ LetterFrequency """
    text = input().replace(" ", "") .lower()
    myset = set(text)
    myset = list(myset)
    number = 0
    for i in range(len(myset)):
        num = text.count(myset[i])
        if num >= number:
            number = num
            ans = myset[i]
    print(ans)
main()

# """ LetterFrequency """
# from typing import numberer

# def main():
#     """ LetterFrequency """
#     txt = str(input())
#     txt1 = numberer(txt)
#     txt2 = txt1.most_common(1)[0][0]
#     print(txt2)
# main()
