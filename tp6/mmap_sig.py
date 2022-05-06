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

# path = '/tmp/archivo.txt'
path = 'file.log'

memoria = mmap.mmap(-1, 100)

# finish = False

def handler_padre(s, f):
    global con
    # print(s == signal.SIGUSR1, '¿es la señal SIGUSR1?') # con esto??
    if s == signal.SIGUSR1:
        linea = memoria.readline()
        print(f'El padre acaba de recibir desde H1: {linea.decode()}')
        os.kill(pidh2, signal.SIGUSR1) # enviar
    if s == signal.SIGUSR2:
        print('El padre le avisar a h2 que tiene que terminar')
        # os._exit(0)
        con = False
        os.kill(pidh2, signal.SIGUSR2)
        # for i in range(1):
        #     print('YYY')
        #     os.wait()
        # os._exit()



def handler_h2(s, f):
    global finish
    if s == signal.SIGUSR1:
        linea = memoria.readline()
        print(f'El H2 acaba de recibir la señal del padre y lee la linea: {linea.decode()}')

        with open(path, 'a') as archivo:
            archivo.write(linea.decode())
            archivo.flush()
    if s == signal.SIGUSR2:
        print('H2 muriendo y avisando al padre')
        # finish = True
        os._exit(0)


pidh1 = os.fork()
if pidh1 == 0:

    print(f'Soy H1 mi pid es: {pidh1} y mi ppid es: {os.getppid()}\n')
    
    for linea in sys.stdin:
        # print(linea == 'bye\n', 'Es igual a bye??')
        if linea == 'bye\n':
            print('H1 muriendo y avisando al padre!')
            os.kill(os.getppid(), signal.SIGUSR2)
            os._exit(0)
        else:
            print(f'H1 acaba de recibir la linea: {linea}')
            memoria.write(linea.encode('ascii'))
            os.kill(os.getppid(), signal.SIGUSR1)

    # os._exit(0)

pidh2 = os.fork()
if pidh2 == 0:
    print(f'Soy H2 y mi pid es: {pidh2} y mi ppdid es: {os.getppid()}\n')
    signal.signal(signal.SIGUSR1, handler_h2)
    signal.signal(signal.SIGUSR2, handler_h2)
    while True:
        signal.pause()

    # os._exit(0)

con = True

# esto es el padre
print(f'Soy el padre y mi pid es: {os.getpid()}\n')
# signal.signal(signal.SIGUSR2, handler_padre)

signal.signal(signal.SIGUSR1, handler_padre)
signal.signal(signal.SIGUSR2, handler_padre)
# while True:
#     if con:
#         signal.pause()
#     else:
#         print('Entra')
#         break

while con:
    signal.pause()
else:
    for i in range(2):
        print(i)
        os.wait()
    print('Padre espero y ahora termina')




