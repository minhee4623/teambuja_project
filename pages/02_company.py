# <법인>
#라디오버튼 -> 법인소재지, 총 체납액
#법인소재지 -> 전국 행정구역 지도 -> 트리맵 
# 총 체납액 드래그하면 히트맵-> 서울만

import streamlit as st
import numpy as np
import plotly.figure_factory as ff
import pandas as pd
import json
from streamlit_folium import st_folium
import folium
import seaborn as sns
import plotly.io as pio # Plotly input output
import plotly.express as px # 빠르게 그리는 방법
import plotly.graph_objects as go # 디테일한 설정
import plotly.figure_factory as ff # 템플릿 불러오기
from plotly.subplots import make_subplots # subplot 만들기
from plotly.validators.scatter.marker import SymbolValidator # Symbol 꾸미기에 사용됨
from urllib.request import urlopen # web이랑 관련된 패키지

# 전국 체납 법인소재지
df = pd.read_csv("./df_com_loc.csv", index_col = 0, encoding='utf8')
df.set_index = df['광역']


st.caption('법인 체납')
st.title("👮‍♀️2022년 :red[법인] 체납 현황👮‍♂️")

page_names = ['전국 체납 법인소재지','서울특별시 구별 총 체납액 집중도']
page = st.radio('원하는 정보를 선택하세요.', page_names)


if page == '전국 체납 법인소재지':
    st.subheader('전국 체납 법인소재지입니다.')
    st.caption('(해당 그래프 색의 진하기는 그래프의 해석과 무관하니 조심~!)')
    # 법인소재지 트리맵
    df_com_loc = pd.read_csv('./df_com_loc2.csv')
    palette = sns.light_palette("#0000CC", n_colors=16).as_hex()
    fig = px.treemap(df_com_loc, path=[px.Constant('all'), '광역'], 
                    values='총 체납액', 
                    color='광역', 
                    color_discrete_sequence =palette
    )
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    st.write(fig)    


else:
    st.subheader('서울특별시 구별 총 체납액 집중도입니다.')
    # 총 체납액 히트맵

    # 서울특별시 구별 총 체납액 - 히트맵
    df1 = pd.read_csv("./df_per_seoul.csv")
    df1.index = df1['지역']
    df1.drop('지역', inplace=True, axis=1)
    geojson = json.load( open('./seoulsigungu.geojson', encoding='utf8') )
    map = folium.Map( location = [37.53, 126.97 ], zoom_start=11, tiles="CartoDB dark_matter" )
    folium.Choropleth(
    geo_data = geojson,
    data = df1,
    columns = [df1.index, '총 체납액'],
    fill_color='YlOrRd',
    # fill_opacity = 0.7,
    # line_opacity=0.5,
    key_on = 'properties.SIG_KOR_NM'
    ).add_to(map)
    # call to render Folium map in Streamlit
    st_data = st_folium(map, width=725)
