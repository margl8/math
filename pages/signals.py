import streamlit as st
import pandas as pd
import plotly_express as px
from app.sgnl import *

time = [0, 0.5, 1, 1.6, 2.1, 2.6, 3.1, 3.4, 3.6, 3.9, 4.2, 4.7, 4.95, 5.24, 5.5, 5.75, 6, 6.28]
amplitude = [0, 0.5, 0.9, 0.98, 0.8, 0.4, -0.8, 1.6, -1.4, -1.6, 1.0, -2.0, 1.1, -1.1, -2.6, 1.8, 0, -1.05]

st.write('ДАНО:' )
st.write('Время:', *time)
st.write('Амплитуда:', *amplitude)

df_signal = pd.DataFrame()
df_signal["Y - Амплитуда"] = [signal(a) for a in amplitude]
df_signal["X - Время"] = [t for t in time]

signal_line_chart = px.line(df_signal, 
                        x="X - Время", y="Y - Амплитуда", 
                        title='Колебания сигнала')
    
st.plotly_chart(signal_line_chart, theme="streamlit")

col1, col2 = st.columns(2)

with col1:
    integral_range_top = st.number_input('Верхний порог интгерала', step=1, value=-25)
with col2:
    integral_range_bottom = st.number_input('Нижний порог интгерала', step=1, value=75)

df_signal["Z"] = [[wavelet(a=a, tau=t, min_length=integral_range_bottom, 
                           max_length=integral_range_top) for a in range(0, len(amplitude), 1)]
                       for t in range(0, len(time), 1)]
signal_3d_chart = go.Figure(data=[go.Surface(z=df_signal['Z'])])
signal_3d_chart.update_traces(contours_z=dict(show=True, usecolormap=True,
                                    highlightcolor="limegreen", project_z=True))
signal_3d_chart.update_layout(title='График сигнала')
    
st.plotly_chart(signal_3d_chart, theme="streamlit")

fig = go.Figure(data =
    go.Contour(z=df_signal["Z"]))

st.plotly_chart(fig, theme="streamlit")
