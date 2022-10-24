"""อยากลองเฉยๆอ่ะครับ"""
def isPrime(num):
	i = 2
	for i in range(2,int(num**0.5) + 1):
		if num%i==0:
			return False
	return True
count = 0

n = int(input())

primes = set()

for num in range(2, n+1):
	if isPrime(num):
		primes.add(num)
semiprimes = set()
semiprimes1 = set()
for i in primes:
	for j in primes:
		prod = i*j
		if prod <= n: 
			semiprimes.add(prod)
		else:
			semiprimes1.add(prod)

print(len(semiprimes))
print((semiprimes))
print(len(semiprimes1))
print((semiprimes1))