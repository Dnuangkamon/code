"""iPhone 13 Again"""

def iphone_pro(num):
    """iPhone_pro"""
    if num == '128 GB':
        ans = 38900
    elif num == '512 GB':
        ans = 50900
    else:
        ans = 58900
    return ans

def main():
    """iPhone 13 Again"""
    num_1 = input()
    num_2 = input()
    if num_1 == 'iPhone 13 mini' and num_2 == '128 GB':
        print(25900)
    elif (num_1 == 'iPhone 13' and num_2 == '128 GB') or \
        (num_1 == 'iPhone 13 mini' and num_2 == '256 GB'):
        print(29900)
    elif num_1 == 'iPhone 13 Pro':
        print(iphone_pro(num_2))
    elif num_1 == 'iPhone 13 Pro Max' and num_2 == '128 GB' or \
        num_1 == 'iPhone 13 Pro' and num_2 == '256 GB':
        print(42900)
    elif num_1 == 'iPhone 13' and num_2 == '256 GB':
        print(33900)
    elif num_1 == 'iPhone 13 Pro Max' and num_2 == '256 GB':
        print(46900)
    elif num_1 == 'iPhone 13 mini' and num_2 == '512 GB':
        print(37900)
    elif num_1 == 'iPhone 13' and num_2 == '512 GB':
        print(41900)
    elif num_1 == 'iPhone 13 Pro Max' and num_2 == '512 GB':
        print(54900)
    elif num_1 == 'iPhone 13 Pro Max' and num_2 == '1 TB':
        print(62900)
    else:
        print('Not Available')
main()
