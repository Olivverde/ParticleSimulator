
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import math
import os
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure




def graph(vel, ang, field):
	xAxis = []
	yAxis= []
	

	#Angulo
	Ang = ang
	#Radianes
	rad = (Ang*math.pi)/180
	#Vel prueba
	Vp = vel
	#Vel x
	Vx = Vp*math.cos(rad)
	#Vel y
	Vy = Vp*math.sin(rad)
	#CampoE
	Campo = field
	#Masa Particula
	masaP = 1.67e-27
	#Carga Particula
	qP = 1.60e-19
	#Elevacion maxima
	hMax = 1e+01
	t = 0e+0
	currentH = 0e+0
	currentX = 0e+0

	while ((currentH<hMax) & ((-hMax)<currentH)):
	    a = (qP*Campo)/masaP
	    currentH = Vy*t+(0.5)*a*(t**2)
	    currentX = Vx*t
	    t += 1e-3
	    xAxis.append(currentX)
	    yAxis.append(currentH)
	d = {'x':xAxis,'y':yAxis}
	df = pd.DataFrame(data=d)
	plt.plot(df['x'], df['y'])
	plt.savefig('static/new_plot.png')
	plt.close()

		
    



