from flask.ext.wtf import Form, RecaptchaField
from wtforms import TextField, BooleanField, PasswordField
from wtforms.validators import Required, EqualTo, Email

class LoginForm(Form):
    openid = TextField('openid', [Required()])
    remember_me = BooleanField('remember_me', default = False)

class RegisterForm(Form):
    name = TextField('NickName', [Required()])
    email = TextField('Email address', [Required(), Email()])
    password = PasswordField('Password', [Required()])
    confirm = PasswordField('Repeate Password',
                            [Required(),
                             EqualTo('password', message='Password must match')
                             ])
    accept_tos = BooleanField('I accept the TOS', [Required()])
    repcaptcha = RecaptchaField()
