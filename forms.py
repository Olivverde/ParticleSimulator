from wtforms import Form
from wtforms import FloatField, StringField, SelectField
from wtforms import validators

class particularInfo(Form):
	Vp = FloatField('Velocity',[validators.Required(message = 'Data is required!')])
	Ang = FloatField('Angle',[validators.Required(message = 'Data is required!')])
	Field = FloatField('Field',[validators.Required(message = 'Data is required!')])
	Width = FloatField('Field Width',[validators.Required(message = 'Data is required!')])
	particle = SelectField('Particle',choices = [('electron','Electron'),('positron','Positron'),
		('proton','Proton'),('tau','Tau'),('antitau', 'Antitau'),('alpha','Alpha Particle'),
		('deuteron','Deuteron'),('muon','Muon'),('antimuon','Antimuon'),('delta','Double Delta Baryon')])