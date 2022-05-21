import getopt, sys, multiprocessing as mp
from math import sqrt, log10

try:
    opt,arg = getopt.getopt(sys.argv[1:], 'p:f:c:')
    if len(opt) != 3:
        print("Por favor ingrese bien la cantidad de argumentos")
        exit()
except getopt.GetoptError as error:
    print(f'Ha habido un error: {error}')
    exit()

cacl: str
num_process: int
path: str
for (op,ar) in opt:
    if op == '-p':
       num_process = int(ar)
    if op == '-f':
        path = str(ar)
    if op == '-c':
        calc = str(ar)

def read_matriz(path):
        file = open(path, 'r')
        lines = file.readlines()
        return lines

def format_lines(path):
    lineas = read_matriz(path=path)
    matriz = [line[:-1] for line in lineas if line is not lineas[-1]]
    matriz.append(lineas[-1])
    num = 0
    for line in matriz:
        matriz[num] = line.split(',')
        num += 1
    return matriz

matriz_nueva = []
def pot(matriz):
    global matriz_nueva
    for fila in matriz:
        nueva_fila = []
        for elemento in fila:
            elemento = int(elemento)**int(elemento)
            nueva_fila.append(elemento)
        matriz_nueva.append(nueva_fila)
    return matriz_nueva

def raiz(matriz):
    global matriz_nueva
    for fila in matriz:
        nueva_fila = []
        for elemento in fila:
            elemento = sqrt(int(elemento))
            nueva_fila.append(elemento)
        matriz_nueva.append(nueva_fila)
    return matriz_nueva

def log(matriz):
    global matriz_nueva
    for fila in matriz:
        nueva_fila = []
        for elemento in fila:
            elemento = log10(int(elemento))
            nueva_fila.append(elemento)
        matriz_nueva.append(nueva_fila)
    return matriz_nueva

calcs = {
    'pot': pot,
    'raiz': raiz,
    'log': log
}

if __name__ == '__main__':
    pool = mp.Pool(processes=num_process)
    # results = pool.map(funcion_calculo, [[[1, 2, 3], [4, 5, 6]]])
    results = pool.map(calcs[calc], [format_lines(path=path)])
    print(results[0])

