import streamlit as st
from services.authors import Authors


# objects and configs.
st.set_page_config(page_title="Team XX", layout="wide")
_authors: Authors = Authors()


# 
st.subheader("CBE Hackathon | Team XX")

with st.container():
    st.write("---")
    # st.subheader("Search")
    # 
    # option = st.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])
    # agree = st.checkbox("I agree to the terms and conditions")
    # age = st.number_input("Enter your age")
    # 
    search_comp_left, search_comp_right = st.columns([2, 1]) 

    with search_comp_left:
        author_names = st.text_input("Enter Author's Names")
    
    with search_comp_right:
        st.write("##")
        search_btn_clicked = st.button("Search")
    
    if search_btn_clicked:
        # --- header ---
        # st.write("---")
        # st.write("###")
        # --- objects ---
        author = _authors.get_author_profile(author_names)
        author_by_id = _authors.search_author(author[0]['author_id'])
        # 
        author_names_col, author_filter_col = st.columns([2,1])
        # author_cites_col, author_email_col = st.columns([2,1])
        # 
        with author_names_col:
            st.write(f"## {author[0]['name']}")
        with author_filter_col:
            st.write("###")
            st.write("Filter")
        st.write("Cited By", author[0]['cited_by'], "\t | \t", author[0]['email'], "\t | \t", author[0]['link'], " | ", author_by_id['author']['affiliations'] )
        # print(author[0])
        
        # 
        # --- citations ---
        # 'author', 'articles', 'cited_by', 'co_authors'
        st.write("---")
        for article in author_by_id['articles']:
            st.write(f"#### {article['title']}")
            st.write(article['link'])
            st.write(article['authors'])
            st.write(article['publication'])
            st.write(article['year'], article['cited_by']['value'] )
            st.write()
            st.write("---")
        
        