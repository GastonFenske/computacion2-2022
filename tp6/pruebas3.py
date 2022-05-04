from concurrent.futures import process
import os, signal, mmap, multiprocessing as mp



def handler_padre():
    print('jojoj')

def main():
    proceso1 = mp.Process(target=target)
    proceso1.start()

    signal.signal(signal.SIGUSR1, handler_padre)
    signal.pause()

def target():
    os.kill(proceso1, signal.SIGUSR1)
    
if __name__ == '__main__':
    main()