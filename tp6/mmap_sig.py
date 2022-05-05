import getopt, sys, os, mmap, signal, time
# try:
#     opt,arg = getopt.getopt(sys.argv[1:], 'f:')
#     if len(opt) != 1:
#         print("Por favor ingrese bien la cantidad de argumentos")
#         exit()
# except getopt.GetoptError as error:
#     print(f'Ha habido un error: {error}')
#     exit()

# for (op,ar) in opt:
#     if op == '-f':
    #    path = str(ar)

# fd_bajo_nievl = os.open(path, os.O_RDWR) # lo abro en bajo nivel y en lectura y escritura

memoria = mmap.mmap(-1, 100)

def handler_padre(s, f):
    linea = memoria.readline()
    print(f'El padre acaba de recibir desde H1: {linea.decode()}')
    
    os.kill(pidh2, signal.SIGUSR1) # enviar

def handler_h2(s, f):
    linea = memoria.readline()
    print(f'El H2 acaba de recibir la señal del padre y lee la linea: {linea.decode()}')

    # with open(,¡....º) as archivo:
    #     archivo.write(....)

pidh1 = os.fork()
if pidh1 == 0:

    print(f'Soy H1 mi pid es: {pidh1} y mi ppid es: {os.getppid()}\n')
    
    for linea in sys.stdin:
        memoria.write(linea.encode('ascii'))
        os.kill(os.getppid(), signal.SIGUSR1)

    os._exit(0)

# pid_h2 = 0
# esto es el padre
pidh2 = os.fork()
if pidh2 == 0:
    print(f'Soy H2 y mi pid es: {pidh2} y mi ppdid es: {os.getppid()}\n')
    # pid_h2  = os.getpid()
    signal.signal(signal.SIGUSR1, handler_h2)
    while True:
        signal.pause()

    # os._exit(0)

# esto es el padre
print(f'Soy el padre y mi pid es: {os.getpid()}\n')
signal.signal(signal.SIGUSR1, handler_padre)
while True:
    signal.pause()
# os.wait()



