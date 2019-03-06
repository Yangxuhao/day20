import multiprocessing
import csv
import os
def getline(path,mylist):
    reader=csv.reader(open(path,"r"))
    lines=0
    for item in reader:
        lines+=1
    print("self pid",os.getpid(),"lines",lines)
    mylist.append(lines)

if __name__=="__main__":
    path=r"D:\尹成python\清华学霸尹成.python基础视频\day23down多线程实战编程\day23down\csv"
    filelist=os.listdir(path)
    processlist=[]
    mylist=multiprocessing.Manager().list()#gongxiang list
    for filename in filelist:
        newpath=path+"\\"+filename
        p=multiprocessing.Process(target=getline,args=[newpath,mylist])
        p.start()
        processlist.append(p)

    for mythd in processlist:
        mythd.join()
    print(mylist)
    print("over")