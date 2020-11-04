from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class ClienteForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    email = EmailField("email", validators=[DataRequired()])
    data_nascimento = DateField("data_nascimento", validators=[DataRequired()], format='%d/%m/%Y')
    profissao = StringField("profissao", validators=[DataRequired()])
    sexo = SelectField("sexo", validators=[DataRequired()], choices=[('M', 'Masculino'), ('F', 'Feminino'),
                                                                     ('N', 'Nenhuma das opções')])