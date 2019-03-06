import multiprocessing
import os
def func(conn):
    conn.send(["a","b","c","d"])
    print(os.getpid(),os.getppid(),conn.recv())
    conn.close()

if __name__=="__main__":
    conn_a,conn_b=multiprocessing.Pipe()
    p=multiprocessing.Process(target=func,args=(conn_a,))
    p.start()
    conn_b.send([1,2,3,4,5])
    print(os.getpid(),os.getppid(),conn_b.recv())
    p.join()