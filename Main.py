from flask import Flask
from flask import render_template
from flask import request
import io
import forms
import Graph
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


app = Flask(__name__, template_folder = "templates")
@app.route('/', methods = ['GET','POST'])

def index():
	particle_form = forms.particularInfo(request.form)
	if request.method == 'POST' and particle_form.validate():	
		fig = Graph.graph(particle_form.Vp.data,particle_form.Ang.data,particle_form.Field.data)
	return render_template('index.html', form = particle_form)
if __name__ == '__main__':
    app.run(debug = True)	