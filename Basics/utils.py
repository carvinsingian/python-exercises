def lbs_to_kg(weight):
	return weight * 0.45


def kg_to_lbs(weight):
	return weight * 2.2


def find_max(numbers):
	maximum = 0
	for number in numbers:
		if number > maximum:
			maximum = number
	return maximum

#finding prime numbers
# L = []
# nmax = 30

# for n in range(2, nmax):
#     for factor in L:
#     	print(n)
#     	print(factor)
#     	if n % factor == 0:
#             break
#     else: # no break
#     	print('hi')
#     	print(n)
#     	L.append(n)
# print(L)