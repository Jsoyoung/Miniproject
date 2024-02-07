# -*- coding:utf-8 -*-

import streamlit as st 
import pandas as pd
from data_collect import load_data
import plotly.express as px
import plotly.graph_objs as go


def groupby_house_type(df):
    def get_building_name(x):
        if pd.notnull(x['BLDG_NM']):
            return f"{x['SGG_NM']} {x['BJDONG_NM']} {x['BLDG_NM']}"
        else:
            return f"{x['SGG_NM']} {x['BJDONG_NM']}"
    
    # 건물 용도별로 그룹화하여 거래금액의 최고가와 최저가, 그리고 건물명을 계산
    result = df.groupby('HOUSE_TYPE').apply(lambda x: pd.Series({
        '최고가': x.loc[x['OBJ_AMT'].idxmax(), 'OBJ_AMT'],
        '최고가 정보': get_building_name(x.loc[x['OBJ_AMT'].idxmax()]),
        '최저가': x.loc[x['OBJ_AMT'].idxmin(), 'OBJ_AMT'],
        '최저가 정보': get_building_name(x.loc[x['OBJ_AMT'].idxmin()])
    })).reset_index()
    
    return result



def home_page(df):
    df = load_data()
    st.subheader("서울시 자치구별 거래건수")
    st.markdown(''':green[서울시 부동산 실거래가 정보 기준] :green[**(접수 기간 : 2020~2023년도)**]''')
    # 자치구별 거래건수 계산
    district_transaction_counts = df.groupby('SGG_NM').size().reset_index(name='거래건수')
    # 거래건수 내림차순 정렬
    district_transaction_counts = district_transaction_counts.sort_values(by='거래건수', ascending=False).reset_index(drop=True)

    # 막대그래프 출력
    fig_district = px.bar(district_transaction_counts, x='SGG_NM', y='거래건수', color='SGG_NM', color_discrete_sequence=px.colors.qualitative.Set3)
    fig_district.update_layout(xaxis_title='자치구', legend_title='자치구')
    st.plotly_chart(fig_district)

    # 가장 거래건수가 많은 자치구
    max_transaction_district = district_transaction_counts.loc[district_transaction_counts['거래건수'].idxmax()]
    
    # 결과 출력
    result_text = f"*자치구명 : {max_transaction_district['SGG_NM']}    *거래건수 : {max_transaction_district['거래건수']} 건"
    st.markdown(':star: :green[**거래건수가 가장 많은 자치구**]')
    st.text(result_text)

    st.markdown('---')
    
    # 건물 용도별 최고가와 최저가 출력
    st.markdown(':star: :green[**주택 용도별 거래가격 정보**]')
    result_df = groupby_house_type(df)
    st.dataframe(result_df)



def details_page(df):
    st.subheader('자치구 용도별 거래건수 막대그래프')

    # 선택한 지역구 및 용도에 따른 데이터 필터링
    selected_sgg = st.sidebar.selectbox('구를 선택하세요.', df['SGG_NM'].unique())
    filtered_df = df[df['SGG_NM'] == selected_sgg]

    selected_house_type = st.sidebar.selectbox('용도를 선택하세요.', df['HOUSE_TYPE'].unique())
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



def main():
    df = load_data()
    st.sidebar.title("대시보드 메뉴")

    with st.sidebar:
        selected = st.sidebar.selectbox("대시보드 메뉴", ['홈', '자세히 보기'])
        st.divider()

    if selected == '홈':
        home_page(df)
    elif selected == '자세히 보기':
        details_page(df)        

    

if __name__ == "__main__":
    main()