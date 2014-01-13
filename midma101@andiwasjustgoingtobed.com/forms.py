from flask.ext.wtf import Form
from wtforms.fields import TextField, PasswordField, BooleanField, FileField
from flask.ext.pagedown.fields import PageDownField
from wtforms.validators import Required, EqualTo, ValidationError

from app import db
from models import User

class PostForm(Form):
    body = PageDownField('body')
    title = TextField('title')
    link = TextField('link')
    image = FileField(u'upload image')
    #picture = TextField('picture', validators = [Required()])

class LoginForm(Form):
    name = TextField('username')
    password = PasswordField('password')
    remember_me = BooleanField('remember_me', default = False)

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise ValidationError('Invalid user')

        if user.pw_hash != self.password.data:
            raise ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(name=self.name.data).first()


class RegisterForm(Form):
    name = TextField('username')
    password = PasswordField('password', [Required(), EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('confirm password')