import streamlit as st
from services.authors import Authors
from services.data_viz import DataViz
import matplotlib.pyplot as plt
import base64
import seaborn as sns


# objects and configs.
st.set_page_config(page_title="Team X", layout="wide")
_authors: Authors = Authors()
_data_viz: DataViz = DataViz()


# 
head_col_1, head_col_2, head_col_3, head_col_4 = st.columns([2,1,1,1])

with head_col_1:
    st.subheader("CBE Hackathon | Team XX")
    
with head_col_2:
    btn_upload_research = st.button("Upload Research")
    
with head_col_3:
    btn_show_cite_year = st.button("Show Citations Per Year")
    
with head_col_4:
    add_research = st.button("Add Research To DB")
    
    



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
        author_names = st.text_input("Enter Author's Names To Search")
    
    with search_comp_right:
        st.write("##")
        search_btn_clicked = st.button("Search")
    
    if search_btn_clicked:
        btn_upload_research = None
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
                # print(option)
            
            st.write("Cited By", author[0]['cited_by'], "\t | \t", author[0]['email'], "\t | \t", author[0]['link'], " | ", author_by_id['author']['affiliations'] )
            # 
            # 'author', 'articles', 'cited_by', 'co_authors'
            # 
            # --- articles ---
            # print(author_by_id['articles'])
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
    
    # 
    # 
    # 
    if btn_upload_research:
        # st.write("Upload Research Document")
        # uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

        # if uploaded_file:
        #     pdf_contents = uploaded_file.read()
        #     print(pdf_contents)

        #     # st.write("File name:", uploaded_file.name)
        #     # st.write("File size:", uploaded_file.size, "bytes")

        #     # st.write("PDF contents:")
        #     # st.write(pdf_contents)
        
        uploaded = st.file_uploader("Please browse for a pdf file", type="pdf")
        # print(uploaded)
        if uploaded is None:
            st.stop()

        base64_pdf = base64.b64encode(uploaded.read()).decode("utf-8")
        pdf_display = (
            f'<embed src="data:application/pdf;base64,{base64_pdf}" '
            'width="800" height="1000" type="application/pdf"></embed>'
        )
        st.markdown(pdf_display, unsafe_allow_html=True)


    # 
    # ---- add research to database ---
    if add_research:
        st.write("Add Research To Db")
        
        
    # --- show number of citations per year ---
    if btn_show_cite_year:
        st.write("### Citations per Year From DB")
        dviz_col1, dviz_col2, dviz_col3 = st.columns([1,1,1])
        ds = _data_viz.cite_year_title()
        fig, ax = plt.subplots(figsize=(8,5))
        sns.barplot(data=ds, x="year", y="cited", order=sorted(ds['year'].unique()) )
        plt.title("Number Of Citations Per Year")
        plt.xlabel("Year Of Publication")
        plt.ylabel("Number Of Citations")
        # plt.show()
        with dviz_col1:
            st.pyplot(plt)
            
        with dviz_col2:
            st.pyplot(plt)
            
        with dviz_col3:
            st.pyplot(plt)
    