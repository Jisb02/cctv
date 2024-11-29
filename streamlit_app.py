import streamlit as st

# CCTV 페이지
st.title("CCTV 모니터링")
st.write("아래 버튼을 눌러 CCTV 영상을 확인하세요.")

# 버튼과 결과 화면
if st.button("3층 복도 CCTV"):
    st.image("CCTV.JPG", caption="3층 복도 CCTV")
    st.write("고장 사유: 파손")

if st.button("인문대 엘리베이터 CCTV"):
    st.image("CCTV.JPG", caption="인문대 엘리베이터 CCTV")
    st.write("고장 사유: 파손")
