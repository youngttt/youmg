import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



st.header('3️⃣ 내 성적 데이터 분석하기 ' , divider='rainbow')
st.subheader('', divider='')

st.subheader('❔ 졸업생들의 대학 합격/불합격 평균등급은?', divider='gray')
def main():
   

    # 파일 업로드
    file_path = 'susi_dch.csv' 
    df = pd.read_csv(file_path)
    plt.rc('font', family='Malgun Gothic')

        # 그룹별 평균값 계산
    mean_by_group = df[['불합', '대학', '전과목', '국영수', '국영수과사', '국영수사', '국영수과']].groupby(['불합', '대학']).mean()
        
        # 결과 표시
    st.subheader('', divider='')
    st.write("🍒대학 그룹별 불/합격별 평균 등급값:", mean_by_group)

if __name__ == "__main__":
    main()
st.subheader('', divider='')
st.subheader('', divider='')

st.subheader('❔ 내가 원하는 대학을 입학한 졸업생들의 평균등급은?', divider='gray')
st.subheader('', divider='')
def main():

    file_path = 'susi_dch.csv' 
    df = pd.read_csv(file_path)
    plt.rc('font', family='Malgun Gothic')

        # 그룹별 평균값 계산
    mean_by_group = df[['불합', '대학', '전과목', '국영수', '국영수과사', '국영수사', '국영수과']].groupby(['불합', '대학']).mean()



    col1, col2, col3 = st.columns(3)
    if col1.button("대학그룹 1"):
        html = mean_by_group.iloc[6].to_frame().T.to_html(index=False)
        st.markdown(f'<div style="display: flex; justify-content: center">{html}</div>', unsafe_allow_html=True)
    if col2.button("대학그룹 2"):
        html = mean_by_group.iloc[7].to_frame().T.to_html(index=False)
        st.markdown(f'<div style="display: flex; justify-content: center">{html}</div>', unsafe_allow_html=True)
    if col3.button("대학그룹 3"):
        html = mean_by_group.iloc[8].to_frame().T.to_html(index=False)
        st.markdown(f'<div style="display: flex; justify-content: center">{html}</div>', unsafe_allow_html=True)

    # 두 번째 줄의 3개 버튼
    col4, col5, col6 = st.columns(3)
    if col4.button("대학그룹 4"):
        html = mean_by_group.iloc[9].to_frame().T.to_html(index=False)
        st.markdown(f'<div style="display: flex; justify-content: center">{html}</div>', unsafe_allow_html=True)
    if col5.button("대학그룹 5"):
        html = mean_by_group.iloc[10].to_frame().T.to_html(index=False)
        st.markdown(f'<div style="display: flex; justify-content: center">{html}</div>', unsafe_allow_html=True)
    if col6.button("대학그룹 6"):
        html = mean_by_group.iloc[11].to_frame().T.to_html(index=False)
        st.markdown(f'<div style="display: flex; justify-content: center">{html}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
st.subheader('', divider='')
st.subheader('', divider='')

st.subheader('❔ 내가 원하는 대학을 가려면 난 몇등급을 올려야 하는가?', divider='gray')
st.subheader('', divider='')

def main():
    
    # 입력 칸을 가로 4개, 세로 2줄로 배치
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        score1 = st.number_input("국어 등급", min_value=0, max_value=100, key='1')
        score5 = st.number_input("영어 등급", min_value=0, max_value=100, key='5')
        score9 = st.number_input("체육 등급", min_value=0, max_value=100, key='9')
    with col2:
        score2 = st.number_input("수학 등급", min_value=0, max_value=100, key='2')
        score6 = st.number_input("과학 등급", min_value=0, max_value=100, key='6')
        score6 = st.number_input("한국사 등급", min_value=0, max_value=100, key='10')
    with col3:
        score3 = st.number_input("사회 등급", min_value=0, max_value=100, key='3')
        score7 = st.number_input("정보 등급", min_value=0, max_value=100, key='7')
    with col4:
        score4 = st.number_input("음악 등급", min_value=0, max_value=100, key='4')
        score8 = st.number_input("미술 등급", min_value=0, max_value=100, key='8')
    st.subheader('', divider='')
    # 평균 계산 버튼
    if st.button("평균등급 계산🕹️"):
        scores = [score1, score2, score3, score4, score5, score6, score7, score8]
        average = sum(scores) / len(scores)
        st.write(f"입력된 점수의 평균은 {average:.2f}점 입니다.")

if __name__ == "__main__":
    main()


st.subheader('', divider='')
st.subheader('', divider='')


st.subheader('❔ 지금의 성적으로 내가 갈 수 있는 대학그룹은?', divider='gray')

import streamlit as st

def main():
    user_number = st.number_input("전과목 평균등급을 입력하세요", min_value=0, max_value=10000)

    # 버튼 클릭 이벤트
    if st.button("내가 갈 수 있는 대학은🎵🚀"):
        if user_number <= 1.58 :
            st.write(f" 당신은 1그룹 대학에 진학 할 수 있어요!! ")
        elif 1.58 < user_number <= 1.628 :
            st.write(f" 당신은 2그룹 대학에 진학 할 수 있어요!! ")
        elif 1.628 < user_number <= 1.916 :
            st.write(f" 당신은 3그룹 대학에 진학 할 수 있어요!! ")
        elif 1.916 < user_number <= 2.56 :
            st.write(f" 당신은 4그룹 대학에 진학 할 수 있어요!! ")
        elif 2.56 < user_number <= 3.35 :
            st.write(f" 당신은 4그룹 대학에 진학 할 수 있어요!! ")
        elif 3.35 < user_number <= 5.22 :
            st.write(f" 당신은 5그룹 대학에 진학 할 수 있어요!! ")
        else:
            st.write(f" 당신은 6그룹 대학에 진학 할 수 있어요!! ")
        
        
        
        
        
        

if __name__ == "__main__":
    main()




st.subheader('', divider='')
st.subheader('', divider='rainbow')