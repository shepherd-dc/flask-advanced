from threading import Thread

from flask import current_app, render_template
from flask_mail import Message


def send_async_mail(app, msg):
    from app import mail
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            raise e

def send_mail(to, subject, template, **kwargs):
    # msg = Message('测试邮件', sender='347928429@qq.com', body='Test', recipients=['1184841288@qq.com'])
    msg = Message('【鱼书】'+subject, sender=current_app.config['MAIL_USERNAME'], recipients=[to])
    msg.html = render_template(template, **kwargs)
    # mail.send(msg)
    app = current_app._get_current_object()
    thr = Thread(target=send_async_mail, args=[app, msg])
    thr.start()