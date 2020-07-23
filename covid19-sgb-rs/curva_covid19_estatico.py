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
linha, = ax.plot([], [], lw=2)

  
plt.xlabel('Dias',fontsize=10)
plt.ylabel('Casos',fontsize=10)
ax.tick_params(axis='both', which='major', labelsize=8)
plt.xticks(np.arange(datetime.date(2020,3,31),datetime.date(2020,7,22),step=datetime.timedelta(days=10)))
plt.yticks(np.arange(0,350,step=25.0))
plt.xlim([datetime.date(2020,3,31), datetime.date(2020,7,22)])
plt.ylim(0, 360)

plt.plot(coronadados.index, coronadados['Confirmados'],color='b',label="Confirmados")
plt.plot(coronadados.index, coronadados['Recuperados'],color='g',label="Recuperados")
plt.plot(coronadados.index, coronadados['Óbitos'],color='r',label="Óbitos")
plt.legend()
plt.savefig('curvas_covid19.png',dpi=300)



