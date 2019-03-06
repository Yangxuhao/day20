import threading
import csv
import os
class mythread(threading.Thread):
    def __init__(self,path):
        self.path=path
        self.line=-1
        threading.Thread.__init__(self)

    def run(self):
        reader = csv.reader(open(self.path, "r"))
        line=0
        for item in reader:
            line+=1
        self.line=line
        print(self.getName(),self.line)
# path=r"D:\尹成python\清华学霸尹成.python基础视频\day23down多线程实战编程\day23down\csv\000001.csv"
# mythd=mythread(path)
# mythd.start()
# mythd.join()
# print(mythd.line)



path=r"D:\尹成python\清华学霸尹成.python基础视频\day23down多线程实战编程\day23down\csv"

filelist=os.listdir(path)
threadlist=[]
for filename in filelist:
    newpath=path+"\\"+filename
    mythd=mythread(newpath)
    mythd.start()
    threadlist.append(mythd)

for mythd in threadlist:
    mythd.join()

linelist=[]

for mythd in threadlist:
    linelist.append(mythd.line)

print(linelist)
