from pandas.core.arrays.categorical import contains
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda_app():
    
    st.subheader('EDA 화면 입니다.')
    
    df = pd.read_csv('data/Car_Purchasing_Data.csv',encoding='ISO-8859-1')
    
    radio_menu = ['데이터프레임','통계치']
    selected_radio = st.radio('선택하세요',radio_menu)
    
    if selected_radio == '데이터프레임' :
        st.dataframe(df)
    elif selected_radio == '통계치' :
        st.write(df.describe())
    
    # 컬럼을 선택하면, 해당 컬럼들만 데이터프레임 표시하는 화면
    selected_columns = st.multiselect('컬럼을 선택하세요',df.columns)
    if len(selected_columns) != 0 :
        st.write(df[selected_columns] )
    else :
        st.write('선택된 컬럼이 없습니다')
        
    # 상관관계 분석을 위한, 상관계수 보여주는 화면 개발
    st.subheader('상관계수')
    # st.write(df[selected_columns].corr())
    
    df_corr = df.iloc[:,3:]
    
    selected_corr =st.multiselect('상관계수 컬럼 선택',df_corr.columns)
    
    # 유저가 1개라도 컬럼을 선택했을 경우
    if len(selected_corr) != 0 :
        st.dataframe(df_corr[selected_corr])
        
        # 상관계수를 수치로도 구하고, 차트로도 표시하라.
        fig1=sns.pairplot(data=df_corr[selected_corr],kind='reg')
        st.pyplot(fig1)
        
    # 유저가 컬럼을 선택하지 않은 경우
    else :
        st.write('선택한 컬럼이 없습니다.')
        
    # 유저가 컬럼을 선택하면,
    # 해당 컬럼의 min과 max에 해당하는 사람이 누구인지
    # 그 사람의 데이터를 화면에 보여주는 기능 개발
    
    ### 문자열 데이터가 아닌, 컬럼들만 가져오는 코드!!!!
    print(df.columns)
    
    print(df.dtypes != object)
    
    print(df.columns[df.dtypes != object])
    
    number_colums = df.columns[df.dtypes != object]
    
    st.subheader('최대 최소에 값에 해당되는 사람 검색')
    selected_minmax_column = st.selectbox('컬럼 선택',number_colums)
    
    # 선택한 컬럼의 최소값에 해당되는 사람의 데이터 출력
    st.write(df.loc[df[selected_minmax_column].min()==df[selected_minmax_column],])   
    # 선택한 컬럼의 최대값에 해당되는 사람의 데어터 출력
    st.write(df.loc[df[selected_minmax_column].max()==df[selected_minmax_column],])
    
    st.subheader('사람 검색')
    # 고객의 이름을 검색할 수 있는 기능 개발
    # 1. 유저한테 검색어 입력을 받습니다.
    name = st.text_input('이름을 입력하세요.')
    # 검색을 위해서 소문자로 변경
    name=name.lower()
    
    # 2. 검색어를 데이터프레임의 Customer Name 컬럼에서 검색해서
    #    가져온다
    df_search = df.loc[df['Customer Name'].str.lower().str.contains(name),]
    
    # 3. 화면에 결과를 보여준다
    st.write(df_search)