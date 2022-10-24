'''Hamming'''

def ham(txt1, txt2):
    '''ham'''
    count = 0
    for i in range(len(txt1)):
        if txt1[i] != txt2[i]:
            count += 1
    print(count)
ham(input(), input())

# """Hamming"""
# def main(txt1, txt2, ans):
#     """Hamming"""
#     for i in range(len(txt1)):
#         if txt1[i] != txt2[i]:
#             ans += 1
#     print(ans)
# main(input(), input(), 0)
