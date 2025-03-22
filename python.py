import streamlit as st # type: ignore
import pandas as pd # type: ignore
import numpy as np # type: ignore
st.tittle("This is our first project")
st.write("This is created by streamlit")

df = pd.DataFrame({'name':["John","Smith","Paul"],'marks':[90,80,70]})
st.write(df)
data = np.array([10,20,30,40,50])
st.line_chart(data)