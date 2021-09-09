import pandas as pd
import csv

file1 = "bright_stars.csv"
file2 = "unit_converted_stars.csv"

d1 = []
d2 = []

with open(file1,"r",encoding="utf8")as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        d1.append(i)
    
with open(file2,"r",encoding="utf8")as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        d2.append(i)
h1 = d1[0]
h2 = d2[0]

stars_d1 = d1[1:]
stars_d2 = d2[1:]

h = h1+h2
stars_d = []
for i in stars_d1:
    stars_d.append(i)
for j in stars_d2:
    stars_d.append(j)

with open("total_stars.csv","w",encoding = "utf8") as f:
    csv_writer = csv.writer(f)

    csv_writer.writerow(h)
    csv_writer.writerows(stars_d)




