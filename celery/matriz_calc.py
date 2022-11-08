from tasks import pot, raiz, log
import getopt, sys

try:
    opt,arg = getopt.getopt(sys.argv[1:], 'f:c:')
    if len(opt) != 2:
        print("Por favor ingrese bien la cantidad de argumentos")
        exit()
except getopt.GetoptError as error:
    print(f'Ha habido un error: {error}')
    exit()

for (op,ar) in opt:
    if op == '-f':
        path = str(ar)
    if op == '-c':
        calc = str(ar)

def read_matriz(path) -> list:
    with open(path, 'r') as file:
        matriz = file.readlines()
        matriz = [line.split(',') for line in matriz]
        return matriz

def calculator(fun, matriz) -> list:
    matriz_nueva: list= []
    for fila in matriz:
        nueva_fila = []
        for elemento in fila:
            elemento = calculate(fun, elemento)
            nueva_fila.append(elemento)
        matriz_nueva.append(nueva_fila)
    return matriz_nueva

def calculate(fun, elemento) -> int:
    functions = {
        'pot': pot.delay(elemento),
        'raiz': raiz.delay(elemento),
        'log': log.delay(elemento)
    }
    return functions[fun]

def main() -> None:
    results = calculator(calc, read_matriz(path))
    print(results)

if __name__ == '__main__':
    main()