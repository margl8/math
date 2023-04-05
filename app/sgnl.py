import pandas as pd
import math as m
import numpy as np
import scipy as sp 
import plotly.express as px
import plotly.graph_objects as go


LENGTH = np.arange(-25,76)
TIME = [0, 0.5, 1, 1.6, 2.1, 2.6, 3.1, 3.4, 3.6, 3.9, 4.2, 4.7, 4.95, 5.24, 5.5, 5.75, 6, 6.28]
AMPLITUDE = [0, 0.5, 0.9, 0.98, 0.8, 0.4, -0.8, 1.6, -1.4, -1.6, 1.0, -2.0, 1.1, -1.1, -2.6, 1.8, 0, -1.05]
df_signal = pd.DataFrame()


#Сигнал задан функцией
def signal(time):
    A = 1
    T = 50
    fi = 0
    omega = (2*m.pi)/T
    f = A * m.sin(omega*time+fi)  #функция сигнала
    return f

def wavelet(a, tau, min_length, max_length):
    def function(time):
        f = 0
        try:
            f = (1/a**0.5) * m.exp(-0.5*((time-tau)/a)**2) * (((time-tau)/a)**2-1) * signal(time)
        except ZeroDivisionError:
            pass
        finally:
            return f
    wave =  sp.integrate.quad(function, min_length, max_length+1)
    return round(wave[0],3)

