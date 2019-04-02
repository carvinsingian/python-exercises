L1 = (1, 2, 3, 4)
L2 = ('a', 'b', 'c', 'd')

z = zip(L1, L2)
print(*z)

l = [val if val%2 else -val
for val in range(20) if val%3]

print(*l)

s = {a%3 for a in range(1000)}
print(*s)

#generators
G = (n**2 for n in range(12))

k = [n for n in G if n<30]
print(k)

#prime number generator

# Generate a list of candidates
L = [n for n in range(2, 40)]

#Remove all multiples of the first value
L = [n for n in L if n==L[0] or n%L[0] > 0]

#Remove all multiples of the second value
L = [n for n in L if n == L[1] or n % L[1] > 0]


#setting up in generator function
def gen_primes(N):
	#generate primes up to N
	primes = set()
	for n in range(2,N):
		if all(n%p > 0 for p in primes):
			primes.add(n)
			yield n

print(*gen_primes(100))