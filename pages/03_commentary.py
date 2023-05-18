import streamlit as st
from PIL import Image


st.balloons()
st.markdown("<h1 style='text-align: center; color: black;'>💸[부자되고싶조]😎</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: green;'>#우미림 #정해정 #이민희 #이주혁</h2>", unsafe_allow_html=True)
st.markdown("***")

st.markdown("<h1 style='text-align: center; color: black;'>주제 선정 이유</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: purple;'>#금융관련 #흥미 #세금체납</h2>", unsafe_allow_html=True)
st.caption('국세청에서 제공하는  상습 고액 체납자 csv 파일을 접하고 이런 종류의 데이터를 정부에서 공개하고 있다는 사실이 굉장히 흥미로웠고, 세금 체납과 세금을 체납한 사람이 주거하고 있는 지역과의 관련성을 시각화를 통해 알아보고 싶었다.')
st.image('image_1.jpg',width=700)
st.image('image_4.jpg',width=700)
st.markdown("***")

st.markdown("<h1 style='text-align: center; color: black;'>작업 과정</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: blue;'>#데이터 전처리 #개인 #법인 #그래프 7개</h2>", unsafe_allow_html=True)
st.caption('개인/ 법인으로 체납 현황데이터를 나눠서 진행하였다. 그리고, 효과적으로 데이터를 보기 위하여 지역별,연령별,연도별 그래프를 만들었다.')
st.image('image_2.jpg',width=700)
st.image('image_3.jpg',width=700)
st.markdown("***")

st.markdown("<h1 style='text-align: center; color: black;'>애먹었던 점</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: orange;'>#코랩 #상대경로 #트리맵 #스승의 은혜</h2>", unsafe_allow_html=True)
st.caption('경로를 설정하고, 공유하는 것에 어려움이 있었다. 구글드라이브를 활용하여 csv파일을 공유함으로써 해결하였다. 또한, 트리맵,히트맵,파이덱에서 문제가 발생하였으나 협업으로 능숙하게 해결하였다.')
st.image('image_6.jpg',width=700)
st.markdown("***")

st.markdown("<h1 style='text-align: center; color: black;'>개선방안</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: green;'>#카테고리 #업종별 #세목별</h2>", unsafe_allow_html=True)
st.caption('챗지피티를 맹신하지 않기로 다짐하였다. 카테고리가 다양하고 데이터의 양이 많아서 전처리 과정에서 처리하지 못했던 점이 아쉬움이 남는다.')
st.markdown("***")

st.markdown("<h1 style='text-align: center; color: black;'>소감</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: brown;'>#힘들었지만 보람 #스트림릿 재미있다 #시각화로 정보얻기</h2>", unsafe_allow_html=True)
st.caption('streamlit으로 간단하게 웹페이지를 구성할 수 있어서 편리하고 좋았다. html보다 적은 코드로 더 화면을 잘 구성할 수 있어서 더 배워서 잘 활용하고 싶다. 강사님이 많이 도와주셔서 무사히 해냈다.')


st.markdown("![Alt Text](https://cdn.class101.net/images/02279595-b8f5-4753-8d57-0000d8ac64ae)")
