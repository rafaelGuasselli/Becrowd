<<<<<<< HEAD
=======
//TODO: Acho que da pra simplificar esse código.

>>>>>>> 1f14772b130092df63a52fd4d3299c942148afc1
def getValue(matriz, pos):
	y, x = pos
	if x >= 0 and y >= 0 and y < len(matriz) and x < len(matriz[y]):
		return matriz[y][x]
<<<<<<< HEAD
	return False

def andar(matriz, pos, caminho, direcao):
	y, x = pos
	if getValue(matriz, (y+1, x)) == 0:

def ex(entrada):
	numLinhas, numColunas = map(int, entrada.split())
	
	pos = (-1, -1)
	matriz = []
	for l in range(0, numLinhas):
		linha = list(map(int, input().split()))
		matriz.append(linha)
		if "X" in linha:
			pos = (l, linha.index("X"))
	
=======
	return -1

def acharProximaPosicao(matriz, pos):
	y, x = pos
	queue = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]
	for posI in queue:
		if getValue(matriz, posI) == "0":
			return posI
	return False

def calcularCaminho(matriz, pos, caminho, direcao):
	y, x = pos
	dy, dx = direcao
	matriz[y][x] = "2"
	horizontal = dx != 0
	proximaPos = acharProximaPosicao(matriz, pos)

	if proximaPos:
		py, px = proximaPos
		proxDirecao = (py-y, px-x)
		if proxDirecao == direcao:
			caminho += "F "
		elif horizontal:
			if direcao == proxDirecao[::-1]:
				caminho += "R F "
			else: 
				caminho += "L F "
		else: 
			if direcao == proxDirecao[::-1]:
				caminho += "L F "
			else: 
				caminho += "R F "

		return calcularCaminho(matriz, proximaPos, caminho, proxDirecao)
	else:
		return caminho + "E"

def ex(entrada):
	qtdLinhas, qtdColunas = map(int, entrada.split())

	posPlayer = (-1, -1)
	matriz = []
	for l in range(0, qtdLinhas):
		linha = input().split()
		if "X" in linha:
			posPlayer = (l, linha.index("X"))
		matriz.append(linha)

	caminho = calcularCaminho(matriz, posPlayer, "", (1, 0))
	print(caminho)
>>>>>>> 1f14772b130092df63a52fd4d3299c942148afc1

while True:
	try:
		entrada = input()
		ex(entrada)
	except EOFError:
		break