from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError

from app.models.user import User

class EmailForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='邮箱格式不正确')])


class LoginForm(EmailForm):
    password = PasswordField(validators=[DataRequired(message='密码不能为空'), Length(6, 32)])


class RegisterForm(LoginForm):
    nickname = StringField(validators=[DataRequired(), Length(2,10, message='昵称长度为2—10个字符')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已被注册')


