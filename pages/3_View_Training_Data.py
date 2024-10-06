import streamlit as st
import pandas as pd
import json


# Load the JSON file
filepath = './data/feedback_mockdata.json'
with open(filepath, 'r') as file:
    json_string = file.read()
    dict_of_feedback = json.loads(json_string)
   
# display the `dict_of_course` as a Pandas DataFrame
df = pd.DataFrame(dict_of_feedback)

for column in df.columns:
    st.write(df[column])