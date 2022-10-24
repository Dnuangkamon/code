"""Password"""
def main():
    """Password"""
    import hashlib
    hux = hashlib.new('sha512')
    hux.update(input().encode('UTF-8'))
    print(hux.hexdigest().upper())
main()
