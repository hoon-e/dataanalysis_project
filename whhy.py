import plotly
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import numpy as np
import ipywidgets as widgets

new_col = ['연도', '나이', '진료과목', '성별', '지역', '아픈날', '병원날', '비율', '총비용', '개인비용', '급여비용', '총일자', '주상병_상세', '부상병_상세', '주상병_분류', '부상병_분류']

chunksize = 10 ** 6
diag = pd.DataFrame(columns=['지역', '나이', '주상병_분류'])
count = 0

dis = set()

for chunk in pd.read_csv('final_diagnosis.csv', names=new_col, sep=",", encoding="cp949", chunksize=chunksize, low_memory=False):

    print(chunk)
    count += 1
    if(count == 1):
        break

fig = px.scatter_matrix(diag, dimensions=["지역", "주상병_분류"])
fig.show()

'''    
disease_dim = go.parcats.Dimension(
    values=diag['주상병_분류'],
    categoryorder='category ascending',
    label="주상병 분류"
)

region_dim = go.parcats.Dimension(
    values=diag['지역'],
    categoryorder='category ascending',
    label="지역"
)

age_dim = go.parcats.Dimension(
    values=diag['나이'],
    categoryorder='category ascending',
    label="나이"
)

#color = diag['지역'];
#colorscale = [['서울특별시', 'aliceblue'],['부산광역시', 'antiquewhite'] ,['대구광역시', 'aqua'] , ['인천광역시', 'aquamarine'], ['광주광역시','azure'], ['대전광역시', 'beige'], ['울산광역시','bisque'], ['세종특별자치시', 'black'], ['경기도', 'blanchedalmond'], ['강원도', 'blue'], ['충청북도', 'blueviolet'], ['충청남도', 'brown'], ['전라북도', 'burlywood'], ['전라남도','cadetblue'], ['경상북도', 'crimson'], ['경상남도','deeppink'], ['제주특별자치도', 'khaki']]

fig = go.Figure(data = [go.Parcats(dimensions=[disease_dim, region_dim, age_dim],
        #line={'color': color, 'colorscale': colorscale},
        #hoveron='color', 
        hoverinfo='count+probability',
        labelfont={'size': 20, 'family': 'Times'},
        tickfont={'size': 18, 'family': 'Times'},
        arrangement='freeform')])

data = [
    go.Parcats(
        dimensions=[disease_dim, region_dim, age_dim],
        line={'color': color,
             'colorscale': colorscale},
        #hoveron='color',
        #hoverinfo='count+probability',
        labelfont={'size': 15, 'family': 'Times'},
        tickfont={'size': 14, 'family': 'Times'},
        arrangement='freeform'
    )
]

fig.show()
'''