import pandas as d
import csv
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split

deathrate = d.read_csv('deathrate_male.csv', names=['main_code', 'region', 'age', 'gender', '2016', '2017', '2018'], sep=",", encoding='utf8')

df = deathrate.groupby(deathrate['main_code']).mean()

X_train, X_test, y_train, y_test = train_test_split(df, df['2016'], random_state=0)

dat = d.DataFrame(X_train, columns=df.index)
print(dat)