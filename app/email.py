#from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from . import mail


#def send_async_email(app, msg):
#    with app.app_context():
#        mail.send(msg)
#    return


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['LP_MAIL_SUBJECT_PREFIX'] + ' ' + subject, sender=app.config['LP_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)
    #print("sender: {}".format(msg.sender))
    #print("recipients: {}".format(msg.recipients))
    #print("body: {}".format(msg.body))
    #thr = Thread(target=send_async_email, args=[app, msg])
    #thr.start()
    #return thr
