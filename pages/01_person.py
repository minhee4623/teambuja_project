## <개인> 
#라디오버튼 ->'연령별 체납 현황','전국 행정구역 체납 지도','서울특별시 구별 총 체납액'
#연령별 (20-29,30-39,40-49,50-59, 60-69,70~) -> 퍼센트로 파이차트
#(2022년도만)체납자 주소 -> 전국 행정구역 지도  -> 트리맵
#총 체납액-> 드래그하면 히트맵 -> 서울만
import streamlit as st
import numpy as np
import plotly.figure_factory as ff
import pandas as pd
import json
from streamlit_folium import st_folium
import folium
import datetime
import matplotlib.pyplot as plt
import matplotlib 
from io import BytesIO
import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns
import math
import pydeck as pdk


st.caption('개인 체납')
st.title("👮‍♀️2022년 :red[개인] 체납 현황👮‍♂️")

page_names = ['연령별 체납 현황','전국 행정구역 체납 그래프','서울특별시 구별 총 체납액 집중도']
page = st.radio('원하는 정보를 선택하세요.', page_names)

if page == '연령별 체납 현황':
    st.subheader('연령별 체납 현황 입니다.')
    st.caption('(총: 31,354명)')
    ## 연령별 파이차트 들어갈 자리
    df = pd.read_csv("./for_pie_chart_df.csv")

    df['sum_ratio'] = df['sum'] / df['sum'].sum()

    labels = ['30대', '40대', '50대', '60대', '70대', '기타']
    values = df['sum_ratio']

    fig = px.pie(df, values=values, names=labels, labels=labels, title='연령대별 체납 현황')

    fig.update_layout(
        autosize=False,
        width=600,  
        height=600  
    )
    st.write(fig)



elif page == '전국 행정구역 체납 그래프':
    st.subheader('전국 행정구역 체납 그래프입니다.')
    st.caption('(해당 그래프 색의 진하기는 그래프의 해석과 무관하니 조심~!)')
    st.caption('(단위: 백만원)')
    ## 전국 행정 구역 체납 트리맵 들어갈 자리
    df_per_loc = pd.read_csv('./df_per_loc2.csv')

    # seaborn 팔레트로 색상톤 조정
    palette = sns.light_palette("#0000CC", n_colors=16).as_hex()

    # 트리맵 
    fig = px.treemap(df_per_loc, path=[px.Constant('all'), '광역'], 
                    values='sum', 
                    color='광역',
                    #color_discrete_map='identity',
                    color_discrete_sequence =palette

                    )
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    st.write(fig)

    st.subheader('전국 체납액 분포도입니다.')
    st.caption('(총 체납액에 제곱근을 취하여 편차를 크게 만들고 효과적으로 시각화하였음)')
    # 전국 체납액 분포도
    df_map_sum = pd.read_csv('./df_map_sum.csv')
    import ast

    # csv를 불러올 때 latlon 열에 있는 위도경도의 값이 list이어야 하는데 str로 인식해버려서 점이 지도에 드러나지 않음
    # 해결: ast라는 모듈에 있는literal_eval함수를 사용하여 list로 변환해줌
    df_map_sum['latlon'] = df_map_sum['latlon'].apply(ast.literal_eval)

    # Use pandas to calculate additional data
    df_map_sum["exits_radius"] = df_map_sum["sum"].apply(lambda exits_count: math.sqrt(exits_count))


    # Define a layer to display on a map
    layer = pdk.Layer(
        "ScatterplotLayer",
        df_map_sum,
        pickable=True,
        opacity=0.8,
        stroked=True,
        filled=True,
        radius_scale=10,
        radius_min_pixels=10,
        radius_max_pixels=100,
        line_width_min_pixels=3,
        get_position="latlon",
        get_radius="exits_radius",
        get_fill_color=[255, 50, 0], 	
        get_line_color=[255, 180, 0],
    )

    # Set the viewport location
    view_state = pdk.ViewState(latitude=37.53, longitude=127.60, zoom=6, bearing=0, pitch=3)

    # Render
    r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{광역}\n{sum}"})
    r.to_html("scatterplot_layer.html")

    # 파이덱사용했으므로 파이덱으로 불러야 함
    st.pydeck_chart(r)








else:
    st.subheader('서울특별시 구별 총 체납액 집중도입니다.')
    # 서울특별시 구별 총 체납액 - 히트맵
    df2 = pd.read_csv("./df_com_seoul.csv")
    df2.index = df2['지역']
    df2.drop('지역', inplace=True, axis=1)
    geojson = json.load( open('./seoulsigungu.geojson', encoding='utf8') )
    map = folium.Map( location = [37.53, 126.97 ], zoom_start=11, tiles="CartoDB dark_matter" )
    folium.Choropleth(
    geo_data = geojson,
    data = df2,
    columns = [df2.index, '총 체납액'],
    fill_color='YlOrRd',
    # fill_opacity = 0.7,
    # line_opacity=0.5,
    key_on = 'properties.SIG_KOR_NM'
    ).add_to(map)
    # call to render Folium map in Streamlit
    st_data = st_folium(map, width=725)
