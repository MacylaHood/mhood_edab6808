import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
st.title("Test run")
variable=st.button("Click me")
if variable:
# Generate random time series data
  time_series = np.random.randn(100)
  fig, ax = plt.subplots()
  ax.plot(time_series)
  ax.set_title("Random 100 time series")
  ax.set_xlabel("Units")
  ax.set_ylabel("Time")
  st.pyplot(fig)


