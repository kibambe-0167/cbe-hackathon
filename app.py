import streamlit as st
from services.authors import Authors
import matplotlib.pyplot as plt


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
    cite_comp_left, cite_comp_right = st.columns([1, 2]) 

    with search_comp_left:
        author_names = st.text_input("Enter Author's Names")
    
    with search_comp_right:
        st.write("##")
        search_btn_clicked = st.button("Search")
    
    if search_btn_clicked:
        author = _authors.get_author_profile(author_names)
        
        if author:
            author_by_id = _authors.search_author(author[0]['author_id'])
            # 
            author_names_col, author_filter_col = st.columns([2,1])
            # author_cites_col, author_email_col = st.columns([2,1])
            # 
            with author_names_col:
                st.write(f"## {author[0]['name']}")
            with author_filter_col:
                st.write("###")
                # st.write("Filter")
                option = st.selectbox("Filter By", ["Year", "Cites", "Title"])
                print(option)
            
            st.write("Cited By", author[0]['cited_by'], "\t | \t", author[0]['email'], "\t | \t", author[0]['link'], " | ", author_by_id['author']['affiliations'] )
            # 
            # 'author', 'articles', 'cited_by', 'co_authors'
            # 
            # --- articles ---
            st.write("---")
            for article in author_by_id['articles']:
                if article['title']:
                    st.write(f"#### {article['title']}")
                if article['link']:
                    st.write(article['link'])
                if article['authors']:
                    st.write(article['authors'])
                if 'publication' in article.keys() and article['publication']:
                    st.write(article['publication'])
                if article['year'] and article['cited_by']['value']:
                    st.write(article['year'], article['cited_by']['value'] )
                st.write("---")
            
            # ---- cited_by ----
            # plot
            # Extract x and y values from the array of dictionaries
            year = [d['year'] for d in author_by_id['cited_by']['graph']]
            cites = [d['citations'] for d in author_by_id['cited_by']['graph']]

            # Create a bar chart using Matplotlib
            fig, ax = plt.subplots(figsize=(5,2))
            ax.bar(year, cites)

            # Set labels and title
            ax.set_xlabel('Year')
            ax.set_ylabel('Citations')
            ax.set_title('Number Of Cites')
            
            with cite_comp_left:
                # Display the plot in Streamlit
                st.pyplot(fig)
            
            with cite_comp_right:
                st.write(f"#### Citations: {author_by_id['cited_by']['table'][0]['citations']['all']}")
                st.write(f"#### h_index: {author_by_id['cited_by']['table'][1]['h_index']['all']}")
                st.write(f"#### i10_index: {author_by_id['cited_by']['table'][2]['i10_index']['all']}")


            
        else:
            st.write("### Author Not Found")
            
    