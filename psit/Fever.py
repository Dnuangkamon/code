"""Fever"""
def main(num):
    """Fever"""
    if num < 36:
        print("hypothermia")
    if 36 <= num < 38:
        print("No Fever")
    if 38 <= num < 39:
        print("Mild Fever")
    if 39 <= num < 40:
        print("High Fever")
    if num >= 40:
        print("Very High Fever")
main(float(input()))
