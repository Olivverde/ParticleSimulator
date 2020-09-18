from wtforms import Form
from wtforms import FloatField, StringField
from wtforms import validators

class particularInfo(Form):
	Vp = FloatField('Velocity',[validators.Required(message = 'Data is required!')])
	Ang = FloatField('Angle',[validators.Required(message = 'Data is required!')])
	Field = FloatField('Field',[validators.Required(message = 'Data is required!')])
	particle = StringField('Particle',[validators.Required(message = 'Data is required!')])