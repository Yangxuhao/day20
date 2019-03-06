import threading
import os

class find(threading.Thread):
    def __init__(self,kaifanglist,istart,iend,searchstr):
        threading.Thread.__init__(self)
        self.kaifanglist=kaifanglist
        self.istart=istart
        self.iend=iend
        self.searchstr=searchstr
    def run(self):
        for i in range(self.istart,self.iend):
            line=self.kaifanglist[i].decode("gbk","ignore")
            if line.find(self.searchstr)!=-1:
                print(self.getName(),line,end="")

path=r"D:\尹成python\kaifangx.txt"
with open(path,"rb") as file:
    kaifanglist=file.readlines()
    lines=len(kaifanglist)
    searchstr=input("input")
    N=10
    threadlist=[]
    for i in range(0,N-1):
        mythd=find(kaifanglist,i*(lines//(N-1)),(i+1)*(lines//(N-1)),searchstr)
        mythd.start()
        threadlist.append(mythd)
    mylastthd=find(kaifanglist,(N-1)*(lines//(N-1)),lines,searchstr)
    mylastthd.start()
    threadlist.append(mylastthd)
    for thd in threadlist:
        thd.join()


    # finddata=find(kaifanglist,0,len(kaifanglist),searchstr)
    # finddata.start()
    # finddata.join()
    # print("over")
#     searchstr=input("input")
#     for line in kaifanglist:
#         line=line.decode("gbk","ignore")
#         if line.find(searchstr)!=-1:
#             print(line)