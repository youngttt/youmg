import streamlit as st




st.header('🏫 난 어떤 대학에 갈 수 있을까?:sunglasses:' , divider='rainbow')
st.text('')
st.image('obje.jpg')
st.text('')
st.text('')


st.subheader(':blossom: 고2가 되는 우리들, 대학정보 어디까지 알고있니?' , divider='rainbow')
video_file = open('intro_univ.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)




from PIL import Image

def main():
    st.title("")

    # 버튼을 추가합니다.
    if st.button('선수 학습 확인🚀'):
      

        # 이미지를 화면에 표시합니다.
        st.image('pre1-1.jpg')
        st.image('pre2.jpg')
        st.image('pre3.jpg')

if __name__ == "__main__":
    main()

