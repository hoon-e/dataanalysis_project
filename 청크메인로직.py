import pandas as d
import csv
import math
col = ['year', 'ssno', 'diagnosis_ssno', 'gender_code', 'age_code', 'region_code', 'start_day', 'seosik', 'subject_code', 'main_disease_code', 'sub_disease_code', 'sick_day', 'hospital_day',  'rate', 'total_pay', 'own_pay', 'insurance_pay', 'total_day', 'pivot_day']

sub_col = ['year', 'age', 'subject', 'gender', 'region', 'start_day', 'main_disease_code', 'sub_disease_code', 'sick_day', 'hospital_day', 'rate', 'total_pay', 'own_pay', 'insurance_pay', 'total_day', 'pivot_day']

m_col = ['year', 'age', 'subject', 'gender', 'region', 'sick_day', 'hospital_day', 'rate', 'total_pay', 'own_pay', 'insurance_pay', 'total_day', 'narrow_disease_name_x', 'narrow_disease_name_y', 'disease_name_x', 'disease_name_y']

new_col = ['year', 'age', 'subject', 'gender', 'region', 'sick_day', 'hospital_day', 'rate', 'total_pay', 'own_pay', 'insurance_day', 'total_day', 'n_disease_name', 'n_sub_disease_name', 'n_main', 'n_sub_name']

chunksize = 10 ** 6

anal_col = ['year', 'age', 'subject', 'gender', 'region_code', 'n_disease_name', 'n_sub_disease_name', 'n_main', 'n_sub_name']
# age = d.read_csv('age_code.csv', names=['age_code', 'age'], sep=",", encoding="cp949")
medic = d.read_csv('의료인원수.csv', names=['age_code', 'ratio'], sep=",", encoding="utf8")
'''
subject = d.read_csv('subject_code.csv', names=['subject_code', 'subject'], sep=',', encoding="cp949")
gender = d.read_csv('gender_code.csv', names=['gender_code', 'gender'], sep=",", encoding='cp949')
'''

region = d.read_csv('region_code.csv', names=['region', 'region_code'], sep=",", encoding='cp949')
'''
code = d.read_csv('code_plus.csv', names=['main_disease_code', 'narrow_disease_name', 'disease_name'], sep=",", encoding="cp949")

code = code.loc[:, ['main_disease_code', 'narrow_disease_name', 'disease_name']]
count = 0
'''
count = 0

for chunk in d.read_csv('diagnosis_second.csv', names=col, sep=",", encoding=, chunksize=chunksize, low_memory=False):
    
    #result = d.merge(chunk, region, on='region', how='left', sort=False)
    print(chunk)
    
    # result.to_csv("./toanal.csv", header=False, sep=",", encoding="cp949", line_terminator="\n", index=False, columns=anal_col, mode="a")
    '''
    result = d.merge(chunk, age, on='age_code', how='left', sort=False)
    result = d.merge(result, subject, on='subject_code', how='left', sort=False)
    result = d.merge(result, gender, on='gender_code', how='left', sort=False)
    result = d.merge(chunk, region, on='region_code', how='left', sort=False)
    '''
    '''
    chunk['main_disease_code'] = chunk['main_disease_code'].map(lambda x : x[0:4])
    chunk['sub_disease_code'] = chunk['sub_disease_code'].map(lambda x : x[0:4])
    
    result = d.merge(chunk, code, on='main_disease_code', how='left', sort=False)
    result = d.merge(result, code, left_on='sub_disease_code', right_on='main_disease_code', how='left', sort=False)
    result = result.fillna("none")
    print(result)
    
    # result = d.merge(chunk, main, on='sub_disease_code', how='left', sort=False)
    # print(chunk)
    result.to_csv("./final_diagnosis.csv", header=False, sep=",", encoding="cp949", line_terminator="\n", index=False, columns=m_col, mode="a")
    # print(result)
    '''
print("끝났씁니다.")