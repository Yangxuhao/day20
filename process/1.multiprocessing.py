import os
import multiprocessing
def info(title):
    print(title)
    print("father ppid",os.getppid())
    print("self pid",os.getpid())
    print("----------")
if __name__=="__main__":
    info("hello")


    p=multiprocessing.Process(target=info,args=("yangxuhao",))
    p.start()
    p.join()
    print("hello 235")