import pandas as d
import csv

main = d.read_csv('main_disease_code.csv', names=['main_disease_code','disease_name'], sep=",", encoding="cp949")
narrow = d.read_csv('narrow_disease_code.csv', names=['narrow', 'narrow_disease_name'], sep=",", encoding="utf-8-sig")
new = d.DataFrame(columns=['code','narrow_disease_name','disease_name'])

print(main)

for n_idx, n in narrow.iterrows():
    for idx, m in main.iterrows():
        if( str(m['main_disease_code']) in str(n['narrow']) ):
            new.loc[n_idx] = [n.narrow, n.narrow_disease_name, m.disease_name]
            # narrow.iloc[n_idx]['main'] = m['disease_name']
            # narrow['main_disease'] = m.Series(m['disease_name'], index=n_idx)

print(new)
new.to_csv("./code_plus.csv", header=False, sep=",", encoding="cp949", line_terminator="\n", index=False, columns=['code', 'narrow_disease_name', 'disease_name'], mode="w")