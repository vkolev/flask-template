from flask.ext.wtf import Form, TextField, PasswordField, BooleanField, TextAreaField
from flask.ext.wtf import Required, Length


class LoginForm(Form):
    username = TextField('username', validators=[Required()])
    password = PasswordField('password', validators=[Required()])
    remember_me = BooleanField('remember_me', default=False)
