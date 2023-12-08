import streamlit as st
import pickle as pkl
import numpy as np

st.title('USA college admission rate')

input_md = open('lr_admit.pkl', 'rb')
model = pkl.load(input_md)
