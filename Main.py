from flask import Flask
from flask import render_template
from flask import request
import io
import forms
import Graph
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


number = 0
url = ''

app = Flask(__name__, template_folder = "templates")
@app.route('/', methods = ['GET','POST'])

def index():
	particle_form = forms.particularInfo(request.form)
	if request.method == 'POST' and particle_form.validate():
		global number
		number += 1
		global url
		url = 'static/new_plot'+str(number)+'.png'
		fig = Graph.graph(particle_form.Vp.data,particle_form.Ang.data,particle_form.Field.data, url)
	return render_template('index.html', form = particle_form, _url = url)
if __name__ == '__main__':
    app.run(debug = True, port = 8000)	