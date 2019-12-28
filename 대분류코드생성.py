import pandas as pd
import csv
import re

col = ['id', 'text', 'pivot', 'disease_code', 'check', 'joo', 'korean', 'english', 'change', 'low', 'explicit', 'rare', 'english', 'korean_plus','default', 'change_text', 'day']

age = pd.read_csv('disease_code.csv', names=col, sep=",", encoding="cp949")

#if(age['pivot'] == "대"):
result = age[['pivot', 'korean']]

count = 0
n = []

output_file = "main_disease_code.csv"
with open("disease_code.csv", "r", newline="", encoding="cp949") as csv_r:
    with open(output_file, "w", newline="", encoding="utf-8-sig") as csv_w:
        writer = csv.writer(csv_w)
        regex = re.compile('\(.+\)')
        
        for row in csv_r:
            row = row.strip()
            row_list = row.split(",")
                
            if(len(row_list) < 3):
                continue
                
            if(row_list[2] == "대"):
                row_list[6] = re.sub(regex, '', row_list[6])
                n.append(row_list[2])
                n.append(row_list[3])
                n.append(row_list[6])
                print(n)
                writer.writerow(n)
                n.clear()
    print("끝")            
    '''
        for i in range(54588):
            if (result.loc[i].pivot == "대"):
        print(result.loc[i].korean)
    '''
        
#result.to_csv("./main_disease_code.csv", header=False, sep=",", encoding="utf-8-sig", line_terminator="\n", index=False, columns=['pivot', 'korean'], mode="a")