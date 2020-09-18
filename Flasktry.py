from flask import Flask
from flask import render_template
from flask import request
import forms

app = Flask(__name__, template_folder = "templates")
@app.route('/', methods = ['GET','POST'])
def index():
	particle_form = forms.particularInfo(request.form)
	if request.method == 'POST' and particle_form.validate():
			print(particle_form.Vp.data)
			print(particle_form.Ang.data)
			print(particle_form.Field.data)
			print(particle_form.particle.data)
	return render_template('index.html', form = particle_form)
if __name__ == '__main__':
    app.run(debug = True)	