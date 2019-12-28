import csv
import pandas as pd
import re

output_file = "narrow_disease_code.csv"
n = list()

with open("disease_code.csv", "r", newline="", encoding="cp949") as csv_r:
    with open(output_file, "w", newline="", encoding="utf-8-sig") as csv_w:
        writer = csv.writer(csv_w)
        regex = re.compile('\(.+\)')
        
        for row in csv_r:
            row = row.strip()
            row_list = row.split(",")
                    
            if(len(row_list) < 3):
                continue
                
            if(row_list[2] == "세"):
                row_list[6] = re.sub(regex, "", row_list[6])
                n.append(row_list[2])
                n.append(row_list[3])
                n.append(row_list[6])
                print(n)
                writer.writerow(n)
                n.clear()
    print("끝")         