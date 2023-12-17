import streamlit as st

st.header('1️⃣ 진로 고민하기 ' , divider='rainbow')
st.subheader('', divider='')
st.subheader('❔ 내가 가고 싶은 대학 생각보기', divider='gray')
st.subheader('', divider='')
title = st.text_input('✔️ :gray[내가 가고 싶은 대학을 입력해보자.]')
st.write('당신이 가고 싶은 대학은', title, '이군요!')


if st.button("✔️대학 그룹확인"):
        group1_universities = ["서울대", "연세대", "고려대", "카이스트", "포항공대"]
        group2_universities = ["성균관대", "서강대", "한양대", "서울교대"]
        group3_universities = ["중앙대", "경희대", "한국외대", "서울시립대", "이화여대"]
        group4_universities = ["홍익대", "건국대"]
        group5_universities = [""]
        group6_universities = [""]

        
        if title in group1_universities:
            st.success(f"{title}는(은) 1그룹에 속합니다.")
        elif title in group2_universities:
            st.success(f"{title}는(은) 2그룹에 속합니다.")
        elif title in group3_universities:
            st.success(f"{title}는(은) 3그룹에 속합니다.")
        elif title in group4_universities:
            st.success(f"{title}는(은) 4그룹에 속합니다.")
        elif title in group5_universities:
            st.success(f"{title}는(은) 5그룹에 속합니다.")
        else:
            st.success(f"{title}는(은) 6그룹에 속합니다.")


st.subheader('', divider='')
st.subheader('', divider='')


st.subheader('❔ 내 성적 확인해보기', divider='gray')


def calculate_average(scores):
    return sum(scores) / len(scores)

def main():
    st.caption('✔️ 나의 전 과목 평균등급을 알아보자.')

    # 과목별 점수 입력
    korean = st.number_input("국어 점수", min_value=0, max_value=100)
    english = st.number_input("영어 점수", min_value=0, max_value=100)
    math = st.number_input("수학 점수", min_value=0, max_value=100)
    science = st.number_input("과학 점수", min_value=0, max_value=100)
    social = st.number_input("사회 점수", min_value=0, max_value=100)
    information = st.number_input("정보 점수", min_value=0, max_value=100)
    music = st.number_input("음악 점수", min_value=0, max_value=100)
    pe = st.number_input("체육 점수", min_value=0, max_value=100)
    art = st.number_input("미술 점수", min_value=0, max_value=100)
    his = st.number_input("한국사 점수", min_value=0, max_value=100)

    # '평균 계산' 버튼 추가
    if st.button('평균 등급 계산🕹️'):
        # 입력된 점수들의 리스트
        scores = [korean, english, math, science, social, information, music, pe, art, his]
        # 평균 계산
        average = calculate_average(scores)
        # 결과 출력
        st.success(f"평균 등급은 {average:.2f}입니다.")

if __name__ == "__main__":
    main()

st.subheader('', divider='')
st.subheader('', divider='')

st.subheader('❔ 우리학교 졸업생들은 어떤 대학에 지원했을까?', divider='gray')


from PIL import Image

def main():
    st.title("")

    # 버튼을 추가합니다.
    if st.button('졸업생 지원 대학list 🧑‍🎓'):
        # 이미지 파일을 엽니다 (예: 'example.jpg')
        image = Image.open('univ_word.png')
       

        # 이미지를 화면에 표시합니다.
        st.image(image)
     
if __name__ == "__main__":
    main()





st.subheader('', divider='rainbow')


