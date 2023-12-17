import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.header('2️⃣ 우리학교 졸업생 입시 데이터 분석하기 ' , divider='rainbow')
st.subheader('', divider='')

st.subheader('❔ 우리학교 수시합격률은?', divider='')
st.subheader('❔ 우리학교 졸업생 대학별 합격/불합격 등급은?', divider='')
st.subheader('❔ 평균등급과 대학별 상관관계는 어떻게 될까?')
st.subheader('', divider='rainbow')


st.subheader('')
st.subheader('✔️ 전처리된 우리학교 졸업생 데이터 업로드', divider='gray')

uploaded_file = st.file_uploader("CSV 파일을 여기에 업로드하세요", type="csv")
if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df.head())

st.subheader('')
st.subheader('')


st.subheader('✔️ 우리학교 수시합격률은?', divider='gray')

file_path = 'susi_dch.csv' 
df = pd.read_csv(file_path)
plt.rc('font', family='Malgun Gothic')

if st.button('수시 합격률'):
        

    # '불합' 열의 빈도수 계산
    counts = df['불합'].value_counts()

    # 빈도수를 사용하여 파이 차트 그리기
    plt.figure(figsize=(8, 6))
    plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # 원형 차트를 그리기 위해 y축의 비율을 같게 설정
    plt.title('우리학교 대학 수시 합격률')  # 차트 제목 설정

    # 차트를 스트림릿에 표시
    st.pyplot(plt)
st.subheader('')
st.subheader('')

st.subheader('✔️ 우리학교 졸업생 대학별 지원 빈도수는?', divider='gray')

if st.button('지원 빈도수'):
        
    counts = df['대학'].value_counts()

        # 빈도수를 사용하여 파이 차트 그리기
    plt.figure(figsize=(8, 6))
    plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # 원형 차트를 그리기 위해 y축의 비율을 같게 설정
    plt.title('대학그룹별 빈도수')  # 차트 제목 설정

    # 차트를 스트림릿에 표시
    st.pyplot(plt)

st.subheader('')
st.subheader('')

st.subheader('✔️ 우리학교 졸업생 대학별 합격/불합격 등급은?', divider='gray')
st.subheader('')
def main():

    # 사용자에게 텍스트 입력 요청
    user_input = st.text_input("🍒 대학별 예상 등급을 생각해보고 작성해보자")

    # 입력값이 있으면 화면에 표시
    if user_input:
        st.write("입력한 내용:", user_input)

if __name__ == "__main__":
    main()
st.subheader('')

def draw_kemss(df):
    plt.figure(figsize=(10, 6))
    sns.catplot(data=df, x="불합", y="국영수과사", hue="대학", kind="bar")
    plt.title("불합에 따른 국영수과사 등급과 대학")
    st.pyplot(plt)

def draw_all(df):
    plt.figure(figsize=(10, 6))
    sns.catplot(data=df, x="불합", y="전과목", hue="대학", kind="bar")
    plt.title("불합에 따른 전과목 등급과 대학")
    st.pyplot(plt)




def draw_kem(df):
    plt.figure(figsize=(10, 6))
    sns.catplot(data=df, x="불합", y="국영수", hue="대학", kind="bar")
    plt.title("불합에 따른 국영수 등급과 대학")
    st.pyplot(plt)


def draw_sc(df):
    plt.figure(figsize=(10, 6))
    sns.catplot(data=df, x="불합", y="과학", hue="대학", kind="bar")
    plt.title("불합에 따른 과학 등급와 대학")
    st.pyplot(plt)


def draw_k(df):
    plt.figure(figsize=(10, 6))
    sns.catplot(data=df, x="불합", y="국어", hue="대학", kind="bar")
    plt.title("불합에 따른 국어 등급과 대학")
    st.pyplot(plt)

def draw_e(df):
    plt.figure(figsize=(10, 6))
    sns.catplot(data=df, x="불합", y="영어", hue="대학", kind="bar")
    plt.title("불합에 따른 영어 등급과 대학")
    st.pyplot(plt)


def draw_m(df):
    plt.figure(figsize=(10, 6))
    sns.catplot(data=df, x="불합", y="수학", hue="대학", kind="bar")
    plt.title("불합에 따른 수학 등급과 대학")
    st.pyplot(plt)

def draw_so(df):
    plt.figure(figsize=(10, 6))
    sns.catplot(data=df, x="불합", y="사회", hue="대학", kind="bar")
    plt.title("불합에 따른 사회 등급과 대학")
    st.pyplot(plt)


chart_type = st.selectbox("🍒원하는 평균등급 과목 선택하세요", ["국영수과사", "전과목", "국영수", "과학", "국어", "영어", "수학", "사회"])
if chart_type == "국영수과사":
    draw_kemss(df)
elif chart_type == "전과목":
    draw_all(df)
elif chart_type == "국영수":
    draw_kem(df)
elif chart_type == "과학":
    draw_sc(df)
elif chart_type == "국어":
    draw_k(df)
elif chart_type == "영어":
    draw_e(df)
elif chart_type == "수학":
    draw_m(df)
elif chart_type == "사회":
    draw_so(df)







st.subheader('✔️ 평균등급과 대학별 상관관계는 어떻게 될까?', divider='gray')
st.subheader('')
txt = st.text_area("🍒등급과 대학은 상관관계가 다음 데이터 분석 결과를 보고 자유롭게 서술해보자",...)

st.write(f'You wrote {len(txt)} characters.')

st.subheader('')



plt.figure(figsize=(8, 6))
sns.regplot(x="국영수", y="대학", data=df)
plt.title("국영수 점수와 대학 관계")
st.pyplot(plt)


filtered_df = df[df["불합"] == 1]
plt.figure(figsize=(8, 6))
sns.regplot(x="국영수", y="대학", data=filtered_df)
plt.title("합격한 학생들의 국영수 점수와 대학 관계")
st.pyplot(plt)


plt.figure(figsize=(10, 6))
sns.relplot(data=df, x="전과목", y="대학", hue="불합", marker="+")
st.pyplot(plt)





st.subheader('', divider='rainbow')