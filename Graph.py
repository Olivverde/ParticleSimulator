
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import math
import os
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure




def graph(vel, ang, field, width, particle, url):
	xAxis = []
	yAxis= []
	
	particles = {'electron':[(-1.60e-19),9.1e-31],'positron':[1.60e-19,9.1e-31],'proton':[1.60e-19,1.67e-27],
				'tau':[(-1.60e-19),3.16e-27],'antitau':[1.60e-19,3.16e-27],'alpha':[3.2e-19,6.64e-27],
				'deuteron':[1.60e-19,3.34e-27],'muon':[(-1.60e-19),1.88e-25],'antimuon':[1.60e-19,1.88e-25],
				'delta':[3.20e-19,2.19e-24]}

	#Angulo
	Ang = ang
	#Radianes
	rad = math.radians(Ang)
	#Vel prueba
	Vp = vel
	#Vel x
	Vx = Vp*math.cos(rad)
	#Vel y
	Vy = Vp*math.sin(rad)
	#CampoE
	Campo = field
	#Masa Particula
	masaP = particles[particle][1]
	#Carga Particula
	qP = particles[particle][0]
	#Elevacion maxima
	hMax = width
	t = 0e+0
	currentH = 0e+0
	currentX = 0e+0

	while ((currentH<hMax) & ((-hMax)<currentH)):
	    a = (qP*Campo)/masaP
	    currentH = Vy*t+(0.5)*a*(t**2)
	    currentX = Vx*t
	    t += 1e-4
	    xAxis.append(currentX)
	    yAxis.append(currentH)
	d = {'x':xAxis,'y':yAxis}
	df = pd.DataFrame(data=d)
	print(df)
	plt.plot(df['x'], df['y'])
	plt.savefig(url)
	plt.close()