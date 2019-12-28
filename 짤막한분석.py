import pandas as d
import csv
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize = (15,15))
# anal = d.read_csv('지역별병수.csv', names=['year', 'age', 'sub', 'gender', 'region', 'main_name', 'sub_name', 'main_code', 'sub_code'], sep=",", encoding="cp949")

rl = d.read_csv('deathrate_male.csv', names=['main_code', 'region', 'age', 'gender', '2016', '2017', '2018'], sep=",", encoding="cp949")

anal = d.read_csv('medical.csv', names=['region', 'ratio'], sep=",", encoding="utf-8-sig")

rl = d.merge(rl, anal, on='region', how='left', sort=False)

s = sns.heatmap(data=rl.corr(), annot=True, fmt= '.2f', linewidths=.5, cmap='Reds')
# reg.to_csv("./지역별병수.csv", header=False, sep=",", encoding="utf8", line_terminator="\n", index=False, mode="w")
