from flask import current_app, render_template
from flask_mail import Message

from app import mail


def send_mail(to, subject, template, **kwargs):
    # msg = Message('测试邮件', sender='347928429@qq.com', body='Test', recipients=['1184841288@qq.com'])
    msg = Message('【鱼书】'+subject, sender=current_app.config['MAIL_USERNAME'], recipients=[to])
    msg.html = render_template(template, **kwargs)
    mail.send(msg)