import csv

with open("1.csv","w",newline="") as datacsv:
    csvw=csv.writer(datacsv,dialect=("excel"))
    csvw.writerow(["1","2","3","4"])
    csvw.writerow(["1", "2", "3", "4"])
    csvw.writerow(["1", "2", "3", "4"])