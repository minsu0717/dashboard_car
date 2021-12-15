import streamlit as st
import pandas as pd
import numpy as np
import joblib

def run_ml_app():
    st.subheader('Machine Learning 예측')
    
    # 1. 유저한테, 데이터를 입력 받습니다.
    gender = st.radio('성별을 입력하세요.',['남자','여자'])
    
    if gender == '남자':
        gender_number = 1
    elif gender == '여자':
        gender_number=0
    
    age = st.number_input('나이 입력',1,120)
    
    salary = st.number_input('연봉 입력',10000)
    
    debt = st.number_input('카드 빚 입력',0)
    
    worth = st.number_input('자산 입력',10000)
    
    print(gender_number,age,salary,debt,worth)
    
    # 2. 모델에 예측한다.
    
    # 2-1. 신규데이터를 넘파이로 만든다.
    new_data = np.array([gender_number,age,salary,debt,worth])
    new_data = new_data.reshape(1,5)
    
    # 2-2. 스케일러와 인공지능을 변수로 불러온다.
    scaler_X = joblib.load('data/scaler_X.pkl')
    scaler_y = joblib.load('data/scaler_y.pkl')
    regressor = joblib.load('data/regressor.pkl')
    
    # 2-3. 신규데이터를 피쳐스케일링 한다.
    new_data = scaler_X.transform(new_data)
    
    # 2-4. 인공지능에게 예측을 하게 한다.
    y_pred = regressor.predict(new_data)
    
    # 2-5. 예측한 결과는, 다시 원래대로 복구해 줘야 한다.
    print(y_pred)
    
    y_pred = scaler_y.inverse_transform(y_pred.reshape(1,1))
    print(y_pred)
    # 3. 예측 결과를 웹 대시보드에 표시한다.
    
    btn = st.button('예측 결과 보기')
    # 결과가 소수점으로 나오는데, 소수점 뒤 한자리까지만 나오도록
    # 코드 수정하세요
    if btn :
        st.write('예측 결과! {} 달러의 차를 살 수 있습니다.'.format(round(y_pred[0,0],2)))
    
    
    
