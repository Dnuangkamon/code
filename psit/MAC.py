""" MAC """
def main():
    """ MAC """
    txt = str(input()).lower()
    txt1 = txt.count('-')
    txt2 = txt.count(':')
    txt3 = txt.count('.')
    for i in txt:
        i = ord(i.lower())
        if 97 <= i <= 102 or 48 <= i <= 57 or i == 58 or i == 45 or i == 46:
            txt = txt
        else:
            txt = "ERROR"
    if txt2 == 0 and txt3 == 0 and len(txt) == 17 and txt1 == 5 and txt.find('-') == 2 and \
        txt.find('-', 3) == 5 and txt.find('-', 6) == 8  and txt.find('-', 9) == 11 \
            and txt.find('-', 12) == 14:
        print('VALID 1')
    elif txt1 == 0 and txt3 == 0 and len(txt) == 17 and txt2 == 5 and txt.find(':') == 2 and \
        txt.find(':', 3) == 5 and txt.find(':', 6) == 8  and txt.find(':', 9) == 11 \
            and txt.find(':', 12) == 14:
        print('VALID 2')
    elif txt1 == 0 and txt2 == 0 and len(txt) == 14 and txt3 == 2 and txt.find('.', 4) == 4 \
        and txt.find('.', 9) == 9:
        print('VALID 3')
    else:
        print('ERROR')
main()
