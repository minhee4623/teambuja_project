## -메인페이지-
# 개인과 법인의 연도별 꺾은선 그래프 총 체납액 추이 (2012-2022)

import streamlit as st
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.io as pio # Plotly input output
import plotly.express as px # 빠르게 그리는 방법
import plotly.graph_objects as go # 디테일한 설정
import plotly.figure_factory as ff # 템플릿 불러오기
from plotly.subplots import make_subplots # subplot 만들기
from plotly.validators.scatter.marker import SymbolValidator # Symbol 꾸미기에 사용됨
from urllib.request import urlopen # web이랑 관련된 패키지

st.markdown("<h1 style='text-align: center; color: red;'>🚨고액 상습 체납자🚨</h1>", unsafe_allow_html=True)

st.image("https://img5.yna.co.kr/mpic/YH/2019/11/20/MYH20191120021500038_P4.jpg",width=700,)
st.text("         ")
st.markdown("***")

st.caption('메인페이지')
st.title('연도별 총 체납액 추이 :blue[(2012-2022)]')
st.caption('(단위:백만원)')
df_year = pd.read_csv("./df_year.csv")
map_ = {'com':'법인', 'per':'개인'}
df_year['split']=df_year['split'].map(map_)
fig = px.line(df_year, x='year', y='sum', color='split') 

st.write(fig)
st.write('**:red[2016년부터는 국세기본법 개정으로 공개기준이 체납국세 5억 원 이상에서 3억 원 이상으로 확대되어 명단공개자가 지난해보다 6.5배 증가하였습니다.]**')
st.caption('[출처] 대한민국 정책브리핑 www.korea.kr')