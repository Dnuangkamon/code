"""BloodDonation"""
def main():
    """BloodDonation"""
    age = int(input())
    weight = int(input())
    times = int(input())
    if age == 17 or (60 <= age <= 70):
        books = str(input())
    else:
        books = "True"
    if 17 <= age <= 70:
        if weight >= 45:
            if (times == 0 and age <= 55) or times > 0:
                if books == "True":
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")
main()
