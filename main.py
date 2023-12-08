import streamlit as st
import pickle as pkl
import numpy as np

st.title('USA college admission rate prediction')

input_md = open('lr_admit.pkl', 'rb')
model = pkl.load(input_md)

st.header('Input admission information')
gre = st.number_input('Insert GRE Score')
toefl = st.number_input('Insert TOEFL Score')
uni_rate = st.number_input('Insert University Rating')
sop = st.number_input('Insert SOP')
lor = st.number_input('Insert LOR')
cgpa = st.number_input('Insert CGPA')
research = st.radio('Choose Research', [0, 1], index=None)
