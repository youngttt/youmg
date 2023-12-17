import streamlit as st

st.header('4️⃣ 분석한 결과로 진로 설계하기 ' , divider='rainbow')
st.subheader('', divider='')


st.subheader('❕ 이번 방학 계획 공유하기', divider='gray')

st.image('qr_code.png')


# 사용자에게 외부 링크 표시
url = "<div style='position: relative; padding-bottom: 56.25%; padding-top: 35px; height: 0; overflow: hidden;'><iframe sandbox='allow-scripts allow-same-origin allow-presentation' allowfullscreen='true' allowtransparency='true' frameborder='0' height='315' src='https://www.mentimeter.com/app/presentation/algjhzh6nzdwroobpbf91b6msmrvv1xo/embed' style='position: absolute; top: 0; left: 0; width: 100%; height: 100%;' width='420'></iframe></div>"
st.markdown(f"[{url}친구들 계획 확인😄](url)", unsafe_allow_html=True)


st.subheader('', divider='')
st.subheader('', divider='')

st.subheader('❕ 목표대학에 진학하기 위해 2,3학년 계획 세우기', divider='gray')
st.subheader('', divider='')
def main():


    # Google 설문조사 URL (여기에 실제 URL을 넣어야 합니다)
    survey_url = "https://forms.gle/Fcn4bk7EUv8GLmx17"

    # 버튼을 클릭하면 Google 설문조사 페이지로 이동
    if st.button("미래 설계하러 가기 🔑 "):
        st.markdown(f"[Google form에 작성하여 제출]({survey_url})", unsafe_allow_html=True)

if __name__ == "__main__":
    main()


st.subheader('', divider='rainbow')