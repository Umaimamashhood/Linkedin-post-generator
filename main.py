import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

length_option = ["Short", "Medium", "Long"]
language_option = ["English", "Hinglish"]  


def main():
    st.title("LinkedIn Post Generator")
    col1, col2, col3 = st.columns(3)
    fs= FewShotPosts()
    with col1:
        tag = st.multiselect("Title:", options= fs.get_tags()) 
    
    
    with col2:
        language = st.selectbox("Language:", language_option)        

    with col3:
        length = st.selectbox(" Post Length:", length_option)

    if st.button("Generate"):
        post = generate_post(length, language, tag)
        st.write(post)

if __name__ == "__main__":  
    main()
        