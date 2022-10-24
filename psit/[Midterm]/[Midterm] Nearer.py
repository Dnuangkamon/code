"""[Midterm] Nearer"""
 
def main():
    """Nearer"""
    alice = int(input())
    bob = int(input())
    ice_cream = int(input())
    if abs(ice_cream - alice) < abs(ice_cream - bob):
        print("Alice %d"% abs(ice_cream - alice))
    elif abs(ice_cream - alice) > abs(ice_cream - bob):
        print("Bob %d"% abs(ice_cream - bob))
    else:
        print("Sundaes %d"% abs(ice_cream - alice))
main()
