import streamlit as st




st.header('🏫 난 어떤 대학에 갈 수 있을까?:sunglasses:' , divider='rainbow')
st.text('')
st.image('obje.png')
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
        # 이미지 파일을 엽니다 (예: 'example.jpg')
        image1 = Image.open('pre1-1.png')
        image2 = Image.open('pre2.png')
        image3 = Image.open('pre3.png')

        # 이미지를 화면에 표시합니다.
        st.image(image1)
        st.image(image2)
        st.image(image3)

if __name__ == "__main__":
    main()

