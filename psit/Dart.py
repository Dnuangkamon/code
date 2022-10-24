"""Dart"""
def main(num, ans):
    """Dart"""
    for _ in range(num):
        dot = input().split()
        num_r = (int(dot[0])**2 + int(dot[1])**2)**0.5
        if num_r <= 2:
            ans += 5
        elif num_r <= 4:
            ans += 4
        elif num_r <= 6:
            ans += 3
        elif num_r <= 8:
            ans += 2
        elif num_r <= 10:
            ans += 1
    print(ans)
main(int(input()), 0)
