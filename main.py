import streamlit as st

st.set_page_config(layout = "wide")

col1, col2 = st.columns(2)

with col1:
    st.image("image/photo.png", width=350)

with col2:
    st.title("Md Arif Uddin")
    content = """
    I am on a mission to channel my fascination with new technology and my passion for data into tangible, positive
    outcomes. I believe that I can be a catalyst for creating a brighter and more inclusive future for us all.
    To prove myself as a quick learner and highly energetic person, I’m ready to face any challenge and also eager to
    build myself as a successful teammate.
    """

    st.info(content)