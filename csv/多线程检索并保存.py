import threading
import os

class find(threading.Thread):
    def __init__(self,kaifanglist,istart,iend,searchstr,savefile):
        threading.Thread.__init__(self)
        self.kaifanglist=kaifanglist
        self.istart=istart
        self.iend=iend
        self.searchstr=searchstr
        self.savefile=savefile
    def run(self):
        self.finlist=[]
        for i in range(self.istart,self.iend):
            line=self.kaifanglist[i].decode("gbk","ignore")
            if line.find(self.searchstr)!=-1:
                self.finlist.append(line)
                print(self.getName(),line,end="")
        global mutex
        with mutex:
            for line in self.finlist:
                self.savefile.write(line.encode("utf-8"))

path=r"D:\尹成python\kaifangx.txt"
mutex=threading.Lock()
savefile=open("wangtao.txt","wb")
with open(path,"rb") as file:
    kaifanglist=file.readlines()
    lines=len(kaifanglist)
    searchstr=input("input")
    N=10
    threadlist=[]
    for i in range(0,N-1):
        mythd=find(kaifanglist,i*(lines//(N-1)),(i+1)*(lines//(N-1)),searchstr,savefile)
        mythd.start()
        threadlist.append(mythd)
    mylastthd=find(kaifanglist,(N-1)*(lines//(N-1)),lines,searchstr)
    mylastthd.start()
    threadlist.append(mylastthd)
    for thd in threadlist:
        thd.join()
savefile.close()