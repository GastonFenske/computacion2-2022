import os, signal, mmap, multiprocessing as mp

memoria = mmap.mmap(-1, 100)

def handler_padre(s, f):
    # linea = memoria.readline().decode()
    # print(linea)
    print('hojojo')
    # print(f'Linea recivida desde el proceso h1: {linea}')

def proceso1_target(linea):
    # print(linea)
    # memoria.write(linea.encode('ascii'))
    os.kill(os.getpid(), signal.SIGUSR1)

linea1 = 'Linea 1 para guardar\n'

def main():
    proceso1 = mp.Process(target=proceso1_target, args=(linea1,))
    proceso1.start()

    print(os.getpid(), 'pid padre')
    print(proceso1.pid, 'pid h1', proceso1._parent_pid)

    signal.signal(signal.SIGUSR1, handler_padre)
    signal.pause()

if __name__ == '__main__':
    main()





