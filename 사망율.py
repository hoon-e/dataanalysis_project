import pandas as d
import re
import csv

rl = d.read_csv('deathrate.csv', names=['why', 'region', 'age', 'gender', 'per', 'how', '2016', '2017', '2018'], sep=",", encoding="cp949")
rl = rl.fillna(0.0)

# rl.to_csv('deathrate2.csv', header=False, columns=['why', 'region', 'age', 'gender', 'per', 'how', '2016', '2017', '2018'], index=False, sep=",", line_terminator="\n", encoding="cp949", mode="w")

count = 1
n = list()
                
with open("deathrate3.csv", "r", newline="", encoding="utf8") as csv_r:
    with open("deathrate_male.csv", "w", newline="", encoding="utf-8-sig") as csv_w:
        writer = csv.writer(csv_w)
        regex = re.compile('\(.+\)')
        
        for row in csv_r:
            row = row.strip()
            row_list = row.split(",")
            
            if( count%2 == 0 ):
                count = count + 1
                continue
            else:
                writer.writerow(row_list)
                count = count + 1
                n.clear()

# for i in range(1, 25839):
#     rl.loc[i].to_csv("./death.csv", header=False, sep=",", encoding="cp949", line_terminator="\n", index=False, columns=['2016', '2017', '2018'], mode="a")
#     i+=4
