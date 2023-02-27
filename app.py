import streamlit as st

st.title("Hello Every one")
st.spinner()

st.markdown("kosetti Narasimha swamy")
st.write("Data Analyst trainee")
st.write("E-mail - knarasimha7999@gmail.com")
st.write("Programming: Python,SQL ")

btn_click = st.button("Click Me!")



if btn_click == True:
    st.subheader("You clicked me :smile:")
    st.balloons()
