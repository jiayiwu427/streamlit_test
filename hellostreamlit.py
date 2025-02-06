import streamlit as st
st.balloons() 
st.title("This is the app title")
st.header("This is the header")
st.markdown("This is the markdown")
st.subheader("This is the subheader")
st.caption("This is the caption")
st.code("x = 2021")

st.number_input('Pick a number', 0, 10)
st.text_input('Email address')
st.date_input('Traveling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')

import matplotlib.pyplot as plt
import numpy as np
rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)