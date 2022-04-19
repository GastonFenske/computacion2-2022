import getopt, sys, os

try:
    opt,arg = getopt.getopt(sys.argv[1:], 'f:')
except getopt.GetoptError as error:
    print(f'Ha habido un error: {error}')
    exit()

for (op,ar) in opt:
    if op == '-f':
        file_to_read = ar

def leer_archivo():
    file = open(file_to_read, 'r')
    return file.readlines()

lineas_recividas = []
def crear_hijo(line):
    if not os.fork():
        os.write(w, line[::-1].encode('ascii'))
        os._exit(0)
    else:
        value = os.read(r, 100)
        lineas_recividas.append(value.decode())


if __name__ == '__main__':
    lines = leer_archivo()
    r, w = os.pipe()
    for line in lines:
        crear_hijo(line)
    
    for line in lines:
        os.wait()

    for line in lineas_recividas:
        print(line)


