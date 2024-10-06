# Set up and run this Streamlit App
import streamlit as st
import pandas as pd
from feedback_handler import feedback_class
import json
import plotly.express as px

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="POC - Feedback Classification"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("POC - Feedback Classification")

col1, col2 = st.columns(2)
response = ''

if 'feedback_dic' not in st.session_state:
    st.session_state.feedback_dic = {}

with col1:
    form = st.form(key="form")
    form.subheader("Prompt")

    user_prompt = form.text_area("Enter your feeback here", height=200)

    if form.form_submit_button("Submit"):
        
        st.toast(f"User Input Submitted - {user_prompt}")

        st.divider()

        response= feedback_class.process_feedback_class(user_prompt)
        response = response.replace('`', '').replace('json', '')

        if len(response) > 10:
            dict_json = json.loads(response)
            dict_json["Original Text"] = user_prompt

            st.session_state.feedback_dic[hash(user_prompt)] = dict_json

            print(st.session_state.feedback_dic)
            
        else:
            st.write("Sorry, unable to extract Category from the given feedback")

        
        st.write("History")
        st.write(st.session_state.feedback_dic)

        #print(response)
        #df = pd.DataFrame(response)
        #df 

        st.divider()

with col2:

    st.write("Category:")

    if(len(st.session_state.feedback_dic) > 0):
        if(len(response) > 10):
            st.write(response)

    summary_dic ={}

    for k, v in st.session_state.feedback_dic.items():
         for x in v.keys():
             summary_dic[x] = 0

    for k, v in st.session_state.feedback_dic.items():
         for x in v.keys():
             summary_dic[x] = summary_dic[x] +1
    
  

    st.write(f"Total Number of Feedback Submitted with Category : {len(st.session_state.feedback_dic)} ")
    #st.write(summary_dic)
    
    df = pd.DataFrame(summary_dic.items(), columns=["Category", "Count"])
    df = df[df["Category"]!='Original Text']


    fig = px.bar(df, x= 'Category', y = 'Count',text_auto=True)
    st.plotly_chart(fig)

    df
    #convert to pfd
    #count categories