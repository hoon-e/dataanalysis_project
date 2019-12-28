import csv
import pandas as pd
import re


output_file = "middle_disease_code.csv"
'''
n = list()

with open("disease_code.csv", "r", newline="", encoding="cp949") as csv_r:
    # with open(output_file, "w", newline="", encoding="utf-8-sig") as csv_w:
        # writer = csv.writer(csv_w)
        for row in csv_r:
            row = row.strip()
            row_list = row.split(",")
                
            if(len(row_list) < 3):
                continue
                
            if(row_list[2] == "중"):
                n.append(row_list[2])
                n.append(row_list[3])
                n.append(row_list[6])
                print(n)
                # writer.writerow(n)
                n.clear()
'''

n = list()
with open("disease_code.csv", "r", newline="", encoding="cp949") as c:
    with open(output_file, "w", newline="", encoding="utf-8-sig") as r:
        writer = csv.writer(r)
        regex = re.compile('\(.+\)')
        
        for row in c:
            row = row.strip()
            row_list = row.split(",")
            
            if(len(row_list) < 3):
                    continue
            if(row_list[2] == "중"):
                row_list[6] = regex.sub("", row_list[6])
                n.append(row_list[2])
                n.append(row_list[3])
                n.append(row_list[6])
                print(n)
                writer.writerow(n)
                n.clear()