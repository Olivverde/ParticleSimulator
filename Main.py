from flask import Flask
from flask import render_template
from flask import request
import os
import forms
from shutil import rmtree
import Graph
from os import remove
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

number = 0
url = ''
flag = 0

app = Flask(__name__, template_folder = "templates")
@app.route('/', methods = ['GET','POST'])

def index():
	particle_form = forms.particularInfo(request.form)
	if request.method == 'POST' and particle_form.validate():
		global number
		global flag
		global url
		if (flag > 0):
			remove(url)
		url = 'static/new_plot'+str(number)+'.png'
		number += 1
		flag += 1
		fig = Graph.graph(particle_form.Vp.data,particle_form.Ang.data,particle_form.Field.data,
			particle_form.Width.data ,particle_form.particle.data, url)
	return render_template('index.html', form = particle_form, _url = url)
if __name__ == '__main__':
	if os.path.isdir('static'):
		rmtree('static')
		os.mkdir('static')
	elif (os.path.isdir('static')) != True:
		os.mkdir('static')

	app.run(debug = True)	