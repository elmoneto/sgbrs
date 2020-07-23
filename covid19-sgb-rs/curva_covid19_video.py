#!/usr/bin/env python
# coding: utf-8

import time
import datetime
import numpy as np
from matplotlib.dates import DateFormatter
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

coronadados = pd.read_csv("dados.csv", index_col="Dia", parse_dates=True)

plt.rcParams["font.family"] = "Roboto"
fig = plt.figure(figsize=(6,6))
plt.title('Evolução da COVID-19 em São Gabriel (RS)',fontsize=12)

ax = plt.gca()
ax.xaxis.grid(True)
ax.yaxis.grid(True)
date_form = DateFormatter("%d/%m")
ax.xaxis.set_major_formatter(date_form)
line, = ax.plot([], [], lw=2)

def animate(i):    
    plt.xlabel('Dias',fontsize=10)
    plt.ylabel('Casos',fontsize=10)
    ax.tick_params(axis='both', which='major', labelsize=8)
    plt.xticks(np.arange(datetime.date(2020,3,31),datetime.date(2020,7,22),step=datetime.timedelta(days=10)))
    plt.yticks(np.arange(0,350,step=25.0))
    plt.xlim([datetime.date(2020,3,31), datetime.date(2020,7,22)])
    plt.ylim(0, 360)
    data = coronadados.iloc[:int(i)]
    linha1,= plt.plot(data.index, data['Confirmados'],label="Confirmados",color="b")
    linha2,=plt.plot(data.index, data['Recuperados'],label="Recuperados",color="g")
    linha3,=plt.plot(data.index, data['Óbitos'],label="Óbitos",color="r")
    plt.legend([linha1,linha2,linha3], ['Confirmados','Recuperados','Óbitos'],loc="upper left")
    return linha1, linha2, linha3

ani = animation.FuncAnimation(fig, animate, interval=500, repeat=False)
Writer = animation.writers['ffmpeg']
writer = Writer(fps=30, metadata=dict(artist='Me'), bitrate=1700)
print('Renderizando o vídeo com ffmpeg')
ani.save('Covid19SG.mp4', writer=writer)


