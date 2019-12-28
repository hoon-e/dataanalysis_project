import pandas as pd
import plotly.graph_objects as go

rl = pd.read_csv('toanal.csv', names=['year', 'age', 'subject', 'gender', 'region', 'main_name', 'sub_name', 'main_code', 'sub_code'], sep=',', encoding="cp949")

reg = rl.groupby('main_code').size()
fig = go.Figure([go.Bar(x=reg.index, y=reg.values)])
fig.show()