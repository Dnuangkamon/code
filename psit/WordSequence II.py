"""WordSequence II"""

def main(word, word1):
    """WordSequence II"""
    word_max = max(len(word), len(word1))
    for i in range(word_max+1):
        print(word1[:i]+word[i:])
main(input(), input())
