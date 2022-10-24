""" [Midterm] Sequence N """
def main():
    """ [Midterm] Sequence N """
    num = int(input())
    for i in range(num):
        for j in range(num):
            if j == 0 or j == num-1 or i == j:
                print("*", end="")
            else:
                print(" ", end="")
        print()
main()
# 4
# *  *
# ** *
# * **
# *  *

# 5
# *   *
# **  *
# * * *
# *  **
# *   *

# 6
# *    *
# **   *
# * *  *
# *  * *
# *   **
# *    *
