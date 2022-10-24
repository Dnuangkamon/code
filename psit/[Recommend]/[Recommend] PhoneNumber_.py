"""[Midterm] PhoneNumber"""
def main():
    """[Midterm] PhoneNumber"""
    phonestr = input()
    area = input()
    if area == 'International':
        phonestr = '+66' + phonestr[1:]
    print(phonestr[:-8], phonestr[-8:-4], phonestr[-4:])
main()
