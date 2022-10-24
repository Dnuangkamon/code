"""BreakPassword"""
def main(text):
    """BreakPassword"""
    import hashlib
    for i in range(100000):
        i = "%05d" % i
        if hashlib.sha512(i.encode("utf-8")).hexdigest().upper() == text:
            print(i)
            break
main(input())