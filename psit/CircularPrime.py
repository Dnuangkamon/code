"""CircularPrime"""
def main(num):
    """function1"""
    count = 0
    for i in range(1, num+1):
        if(num % i == 0):
            count += 1
    if(count == 2):
        return 1
    else:
        return 0

digit=0
i=0
rem=0
sum=0
check=input("enter the number: ")
length=len(check)
num=int(check)
while(i<length):
    rem=int(num % 10)
    num=int(num / 10)
    num=int((rem * (10 ** (length - 1)) + num))
    print(num)
    digit=main(num)
    sum=sum+digit
    i+=1
if(sum==length):
    print("Circular Prime")
else:
    print("Non-Circular Prime")
