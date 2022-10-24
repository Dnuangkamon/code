"""PairNumbering"""
import json
def main():
    """Timeout"""
    a_list = json.loads(input())
    b_list = json.loads(input())
    num = int(input())
    ans = 0
    test = 0
    for i in a_list:
        for j in b_list:
            test = i+j
            if test == num:
                ans += 1
    print(ans)
main()
