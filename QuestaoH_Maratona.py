def main()
	quantidade_original = int(input())
	quantidade_suspeita = int(input())
	notas_original = input()
	notas_suspeito = input()
	if plagio(quantidade_original, quantidade_suspeita, notas_original, notas_suspeito):
		print("S")
	else:
		print("N")

def plagio(n1, n2, original, suspeito):
	dicionario = {"C": 1, "C#": 1.5, "Db": 1.5, "D": 2, "E": 3, "F": 4, "G": 5, "A": 6, "B": 7}
	
	for i in range(n1):
		intervalos_originais.append(dicionario[string[notas_originais[i + 1]]] - dicionario[string[notas_originais[i]]])

	for i in range(len(n2):
		intervalos_suspeitos.append(dicionario[string[notas_originais[i + 1]]] - dicionario[string[notas_originais[i]]])

	i = 0
	resultado = False:
	for i in range