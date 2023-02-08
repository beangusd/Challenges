def list_of_multiples(num, length):
	multiples = []
	for i in range(1, length):
		multiples.append(num * i)
	return multiples
print(list_of_multiples(7, 10))