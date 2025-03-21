import streamlit as st

def show():
    st.header('About')
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("images/aditi_pic.jpg", caption="Machine Learning Engineer", use_column_width=True)
        st.markdown("""
        ### Aditi Singh

        An experienced software developer with expertise in Python and Machine Learning.
        """)

