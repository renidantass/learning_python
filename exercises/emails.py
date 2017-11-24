# coding:utf-8
"""
    Create a software that manages emails and send emails to all @gmail
"""
from email.MIMEMultipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email.MIMEText import MIMEText
from random import randint
from os import path
import smtplib


class Sender(object):
    """
        Wrapper to send emails via Gmail
    """
    def __init__(self):
        self._server = smtplib.SMTP('smtp.gmail.com', 587)
        self._server.starttls()
        self._from_email = "pontosdevista3a@gmail.com"
        self._login()
        self.message = MIMEMultipart()
        self.message['From'] = self._from_email
        self.subject = self.message['Subject'] = '''Convite para exposição de Arte [3ºA]'''
        # MIMETEXT
        self.photo = 'ingresso.png'

    def _login(self):
        """
            Login on server
        """
        self._server.login(self._from_email, "terceiroa")

    def send(self, to_email=None):
        """
            Send email to_email
        """
        img = MIMEImage(open('ingresso.png').read())
        img.add_header('Content-ID', '<{}>'.format(self.photo))
        self.psswd = randint(1000, 9999)
        self.text=  MIMEText('''<strong>Seja bem-vindo(a)</strong> à nossa exposição de Arte,
esperamos que aprecie-a.<br/><h2>Sua senha: %s</h2><br/><img src="cid:%s"><br/>''' % (self.psswd, self.photo), 'html')
        self.message['To'] = to_email
        self.message.attach(self.text)
        self.message.attach(img)
        result = self._server.sendmail(self._from_email, to_email, self.message.as_string())
        print 'Email enviado!'
        return to_email, self.psswd

def load_many(file):
    """
        Load emails from dat file
    """
    emails = []
    if path.exists(file):
        with open(file, 'rb') as f:
            emails = [line for line in f.readlines()]
        return emails
    return -1


emails = load_many('emails.dat')
data = [] # get pass sended to email

# Gmail sender
sender = Sender()

for email in emails:
    email_retrieved, psswd = sender.send(email)
    temp_data = {'email': email_retrieved, 'pass': psswd}
    data.append(temp_data)
    print 'Senha {} enviada para {}'.format(psswd, email)
    with open('sended.csv', 'w') as f:
        f.write('{}:{}\n'.format(email, psswd))

print data
