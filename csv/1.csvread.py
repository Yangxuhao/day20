import csv
path=r"D:\尹成python\清华学霸尹成.python基础视频\day23down多线程实战编程\day23down\csv\000001.csv"
reader=csv.reader(open(path,"r"))
money=0
line=0
for item in reader:
    if line>0:
        money=money+eval(item[13])
    line+=1
print(money)
print(line)