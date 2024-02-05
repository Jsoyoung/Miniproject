# -*- coding:utf-8 -*-

import streamlit as st 
import pandas as pd
from data_collect import load_data
import plotly.express as px



def main():
    df = load_data()
    st.subheader('지역구 용도별 거래건수 막대그래프')
    st.markdown(''':green[서울시 부동산 실거래가 정보 기준] :green[**(접수 기간 : 2020~2023년도)**]''')

    # 선택한 지역구 및 용도에 따른 데이터 필터링
    selected_sgg = st.selectbox('구를 선택하세요.', df['SGG_NM'].unique())
    filtered_df = df[df['SGG_NM'] == selected_sgg]

    selected_house_type = st.selectbox('용도를 선택하세요.', df['HOUSE_TYPE'].unique())
    filtered_df = filtered_df[filtered_df['HOUSE_TYPE'] == selected_house_type]

    # 거래건수 계산
    transaction_counts = filtered_df.groupby('BJDONG_NM').size().reset_index(name='거래건수')
    # 거래건수 내림차순 정렬
    transaction_counts = transaction_counts.sort_values(by='거래건수', ascending=False).reset_index(drop=True)
    

    # 막대그래프 출력
    fig = px.bar(transaction_counts, x='BJDONG_NM',  y='거래건수', color='BJDONG_NM',
                 title=f'{selected_sgg}의 {selected_house_type} 거래건수')

    fig.update_layout(xaxis_title='법정동 이름', legend_title='법정동 이름')

    st.plotly_chart(fig)

    # 표 출력
    transaction_counts.index = transaction_counts.index + 1
    transaction_counts.rename(columns={'BJDONG_NM' : '법정동 이름'}, inplace=True)
    checkbox = st.checkbox("위 차트를 표로 보기")

    if checkbox:
        st.dataframe(transaction_counts)

    # 거래량 높은 순대로 3개만 출력
    st.markdown("---")
    st.markdown(''':star: :green[**거래량 3순위**]''')
    st.dataframe(transaction_counts.head(3))



if __name__ == "__main__":
    main()