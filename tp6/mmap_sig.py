import getopt, sys, os, mmap, signal, time
try:
    opt,arg = getopt.getopt(sys.argv[1:], 'f:')
    if len(opt) != 1:
        print("Por favor ingrese bien la cantidad de argumentos")
        exit()
except getopt.GetoptError as error:
    print(f'Ha habido un error: {error}')
    exit()

for (op,ar) in opt:
    if op == '-f':
       path = str(ar)

# fd_bajo_nievl = os.open(path, os.O_RDWR) # lo abro en bajo nivel y en lectura y escritura

memoria = mmap.mmap(-1, 100)

def handler_padre(s, f):
    linea = memoria.readline()
    print(f'El padre acaba de recibir desde H1: {linea.decode()}')

    os.kill(hijos_pidds[1], signal.SIGUSR1) # enviar

def handler_h2_creado():
    linea = memoria.readline()
    with open(,¡....º) as archivo:
        archivo.write(....)

# def handler_h2(s, f):
#     linea = memoria.readline()
#     print(f'El proceso H2 acaba de recibir la señal USR1 del padre y escribira en el archivo la siguiente linea: {linea.decode()}')

linea1 = 'hola soy la linea 1\n'
linea2 = 'hola soy la linea 2\n'
hijos_pidds = []

pidh1 = os.fork():
if pidh1 ==0:
    # hijos_pidds.append(pid)
    # print(hijos_pidds)
    # print(os.getpid())
    print(f'Soy H1 mi pid es: {pidh1} y mi ppid es: {os.getppid()}')
    # print(f'Soy el H1 escribiendo: {linea1}')
    for linea1 in sys.stdin:

        memoria.write(linea1.encode('ascii'))
        os.kill(os.getppid(), signal.SIGUSR1)
        
    # signal.signal(signal.SIGUSR2, handler_h2_creado)
    # signal.pause()
    time.sleep(2)

    # if os.getpid() == hijos_pidds[0]:
    #     print(f'Soy el H1 escribiendo: {linea1}')
    #     memoria.write(linea1.encode('ascii'))
    #     os.kill(os.getppid(), signal.SIGUSR1)
    os._exit(0)

# esto es el padre
pidh2 = os.fork()
if pidh2 ==0:
    signal.signal(signal.SIGUSR1, handler_h2)
    while True:
        signal.pause()
    # print(pidh1, 'pidh1 en h2')
    pid = os.getpid()
    # os.kill(pidh1, signal.SIGUSR2)
    # hijos_pidds.append(pid)
    print(f'Soy H2 mi pid es: {pid} y mi ppi es: {os.getppid()}')
    os._exit(0)

# esto es el padre
# os.wait()
print(f'Soy el padre y mi pid es: {os.getpid()}')
signal.signal(signal.SIGUSR1, handler_padre)
while True:
    signal.pause()
os.wait()



        

    

# if os.getpid() == hijos_pidds[1]:
#     print('Soy el H2 reciviendo')
#     signal.signal(signal.SIGUSR1, handler_h2)
#     signal.pause() 
# exit()


# signal.signal(signal.SIGUSR1, handler_padre) # recibir
# signal.pause() # espera para recibir

# os.wait()


