"""Pad Thai"""
def padthai():
    """ฟังก์ชั่น Pad Thai"""
    set_staple, set_taste = set(), set()
    set_staple1 = {'Peanuts', 'Oil', 'Egg', 'Pickle Turnip', 'Pad Thai Sauce', \
        'Bean Sprouts', 'Noodle', 'Chives', 'Lime', 'Tofu', 'Shrimp'}
    set_taste1 = {"Sweet", "Sour", "Salty"}
    while True:
        staple = input()
        if staple == 'Cook':
            break
        set_staple.add(staple)
    while True:
        taste = input()
        if taste == 'End':
            break
        set_taste.add(taste)
    total_staple = set_staple1.difference(set_staple) #วัตถุดิบขาด
    total_staple1 = set_staple.difference(set_staple1) #วัตถุดิบเกิน
    total_taste = set_taste1.difference(set_taste) #รสชาติไม่ครบ
    total_taste1 = set_taste.difference(set_taste1) #รสชาติเกิน
    if total_staple == set() and total_staple1 == set():
        if total_taste == set() and total_taste1 == set():
            print('Delicious!')
        else:
            print('Not Bad...')
    else:
        if total_staple1 != set():
            print('This is not Pad Thai!!!')
        elif total_staple != set():
            print('This is bad!')
padthai()
