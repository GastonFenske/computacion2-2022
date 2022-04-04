import getopt, sys, os

try:
    opt,arg = getopt.getopt(sys.argv[1:], 'n:h:v:')
except getopt.GetoptError as error:
    print(f'Ha habido un error: {error}')
    exit()

for (op,ar) in opt:
    if op == '-n':
        num_hjos = int(ar)
    elif op == '-h':
        print("Ayuda")
    elif op == '-v':
        print("Modo verboso")

def hijo():     
    if not os.fork():
        suma = sum([i for i in range(os.getpid()) if i % 2 == 0])
        print(f'{os.getpid()} - {os.getppid()}: {suma}')
        os._exit(0)

for i in range(num_hjos):
    hijo()


