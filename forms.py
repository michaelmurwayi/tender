from flask_wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email

class SupplierForm(Form):
    suppliername = StringField('SupplierName', validators=[DataRequired()])
    tendertype = StringField('TenderType', validators=[DataRequired()])
    contactemail = StringField('ContactEmail', validators=[DataRequired(), Email()])
    phonenumber = IntegerField('PhoneNumber', validators=[DataRequired])
    technicalrequirement = StringField('technicalrequirement', validators=[DataRequired()])
    mandatoryrequirement = StringField('mandatoryrequirement', validators=[DataRequired()])