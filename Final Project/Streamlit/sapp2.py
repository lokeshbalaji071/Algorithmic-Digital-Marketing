#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import os
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image



st.title('Apple iPhone Review System')
st.write('----------------------------------------------------------------------------------------------------------------------------')
st.markdown('This application is meant to **_assist_ _Customers_ _in_ Choosing an iPhone model based on Reviews**, The customers would detrmne the purchase of their iphone models based on previous customer purchases')

imagg = Image.open('C:\\Users\\lokes\\srcs\\streamlit_app\\images_1.jpg')
st.image(imagg, width=None)

df = pd.read_csv('C:\\Users\\lokes\\srcs\\streamlit_app\\result.csv')
df1 = pd.read_csv('C:\\Users\\lokes\\srcs\\streamlit_app\\ReviewCount.csv')

def get_splited_df_dict(df: 'pd.DataFrame', split_column: 'str'):
    """
    splits a pandas.DataFrame on split_column and returns it as a dict
    """

    df_dict = {value: df[df[split_column] == value] for value in df[split_column].unique()}

    return df_dict

splitted = get_splited_df_dict(df, "PRODUCT")
splitted_1 = get_splited_df_dict(df1, "Products")
if st.checkbox('Show me Training Data'):
	st.dataframe(df)
   
st.markdown('Please **Enter _the_ _below_ details** to know the results -')

with st.form(key = "form1"):
    _input = str(st.text_input(label="Enter Model to Search"))

    storage_ls = ['Select Option', '(32GB)', '(64GB)', '(128GB)', '(256GB)', '(512GB)']
    stro = st.selectbox('Storage', storage_ls)


    colour_ls = ['Select Option', 'Gold', 'Black', 'Rose Gold', 'White', 'Green', 'Graphite', 'Purple', 'Blue', 'Space Grey', 'Pacific Blue', 'Red']
    colour = st.selectbox('Colour', colour_ls)
    
    review_ls = ['Select Option', 'All Reviews', 'Positive', 'Negative']
    review = st.selectbox('Review Analysis', review_ls)

    #input = _input+stro+'-'+colour
    
    submit= st.form_submit_button('Check Reviews')
    input = _input+' '+stro+' - '+colour
    
    
st.text(input)

    #if st.button('Check Reviews'):
n=0
for index, row in df.iterrows():
    if (row["PRODUCT"] == input)and n==0:
        des_df = splitted['%s'%(input)]
        st.subheader('Customer Reviews about the model')
        if(review == 'All Reviews'):
            des_df["DESCRIPTION"]
        else:
            comm_df =des_df [des_df["ANALYSIS"] == '%s'%review]['DESCRIPTION']
            comm_df
        n+=1

        #st.button('jshjhsjdhu')
n=0
for index, row in df1.iterrows():
    if (row["Products"] == input)and n==0:
        pos_df = splitted_1['%s'%(input)]
        st.subheader('Total Positive Reviews')
        pos_df["Positive"]
        st.subheader('Total Negative Reviews')
        pos_df["Negative"]
        pos_df.reset_index(drop=True, inplace=True)
        n+=1
        
        #submit= st.form_submit_button('Check Reviews')

