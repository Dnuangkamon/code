"""OneTwo"""
def main(onetwo):
    """ฟังก์ชั่น OneTwo"""
    if onetwo == 1:
        return "1"
    elif onetwo == 2:
        return "2"
    else:
        return main(onetwo-1) + main(onetwo-2)
print(main(int(input())))
