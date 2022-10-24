"""[Midterm] FourDirections"""
def main():
    """[Midterm] FourDirections"""
    arrow_u = ["  *  ",
               " *** ",
               "* * *",
               "  *  ",
               "  *  "]
    arrow_d = ["  *  ",
               "  *  ",
               "* * *",
               " *** ",
               "  *  "]
    arrow_l = ["  *  ",
               " *   ",
               "*****",
               " *   ",
               "  *  "]
    arrow_r = ["  *  ",
               "   * ",
               "*****",
               "   * ",
               "  *  "]
    txt = input()
    for i in range(5):
        for letter in txt:
            if letter == "U":
                print(arrow_u[i], end=" ")
            if letter == "D":
                print(arrow_d[i], end=" ")
            if letter == "L":
                print(arrow_l[i], end=" ")
            if letter == "R":
                print(arrow_r[i], end=" ")
        print()
main()

# UDLLR
#   *     *     *     *     *   
#  ***    *    *     *       *  
# * * * * * * ***** ***** ***** 
#   *    ***   *     *       *  
#   *     *     *     *     *