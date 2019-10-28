matriz = [
	[10, 20, 30, 40],
	[50, 60, 70, 80],
	[90, 100, 110, 120]
]

print(matriz[0][0])

vetor = [10, 20, 30, 40, 50]

print(vetor[-1])


matriz = [
	['joao', 8, 7, 6],
	['pedro', 4.5, 9, 10],
	['marcos', 6, 6, 8]
]

for linha in matriz:
	print(linha)

print('')

for linha in matriz:
	for col in linha:
		print(str(col) + '\t', end = '')
	print('')