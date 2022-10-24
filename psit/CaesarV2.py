"""CaesarV2"""
def main():
    """CaesarV2"""
    text = input()
    result = ""
    for i in range(26):
        for k in range(len(text)):
            char = text[k]
            if char.isupper():
                result += chr((ord(char) + i - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) + i - 97) % 26 + 97)
            else:
                result += char
        if result.count('The') > 0 or result.count('the') > 0:
            break
        else:
            result = ""
    print(result)
main()

"""Caesar"""
def main():
    """main function"""
    message = input()
    for num in range(26, 0, -1):
        new_message = ""
        for i in message:
            ascii_num, lowertxt = ord(i) + (num % 26), i.islower()
            if (lowertxt and ascii_num < 97) or (not lowertxt and ascii_num < 65):
                ascii_num += 26
            elif (lowertxt and ascii_num > 122) or (not lowertxt and ascii_num > 90):
                ascii_num -= 26
            new_message += chr(ascii_num) if i.isalpha() else i
        if "the" in new_message.lower().split():
            print(new_message)
            break
main()