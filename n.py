import sys
import csv 

#input_file = "diagnosis_no_head.csv"
input_file = "disease_code.csv"
count = 0

with open(input_file, "r", newline="", encoding="utf-8-sig") as csv_f:
    #with open(output_file, "w", newline="") as csv_r:
        # header = csv_f.readline()
        # header = header.strip()
        # header_list = header.split(",")
        # print(header)
        
        for row in csv_f:
            row = row.strip()
            row_list = row.split(",")
            
            count += 1
            
            print(row)
            
            if(count == 30):
                break
            '''
            writer = csv.writer(csv_r)
            writer.writerow(row_list)
            '''
        print("끝")    