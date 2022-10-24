"""TicTacToe"""
def main():
    """TicTacToe"""
    line1, line2, line3 = input(), input(), input()
    ans = "DRAW"
    if (line1[0] == "O" and line1[1] == "O" and line1[2] == "O") or\
    (line2[0] == "O" and line2[1] == "O" and line2[2] == "O") or\
    (line3[0] == "O" and line3[1] == "O" and line3[2] == "O") or\
    (line1[0] == "O" and line2[0] == "O" and line3[0] == "O") or\
    (line1[1] == "O" and line2[1] == "O" and line3[1] == "O") or\
    (line1[2] == "O" and line2[2] == "O" and line3[2] == "O") or\
    (line1[0] == "O" and line2[1] == "O" and line3[2] == "O") or\
    (line1[2] == "O" and line2[1] == "O" and line3[0] == "O"):
        ans = "O WIN"
    if (line1[0] == "X" and line1[1] == "X" and line1[2] == "X") or\
    (line2[0] == "X" and line2[1] == "X" and line2[2] == "X") or\
    (line3[0] == "X" and line3[1] == "X" and line3[2] == "X") or\
    (line1[0] == "X" and line2[0] == "X" and line3[0] == "X") or\
    (line1[1] == "X" and line2[1] == "X" and line3[1] == "X") or\
    (line1[2] == "X" and line2[2] == "X" and line3[2] == "X") or\
    (line1[0] == "X" and line2[1] == "X" and line3[2] == "X") or\
    (line1[2] == "X" and line2[1] == "X" and line3[0] == "X"):
        ans = "X WIN"
    print(ans)
main()
