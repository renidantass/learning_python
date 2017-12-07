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
import csv


class Filer(object):
    def __init__(self):
        self.file = 'inscritos.csv'
        self.people = {}

    def load_many(self):
        """
            Load emails from csv file
        """
        if path.exists(self.file):
            with open(self.file, 'rb') as f:
                emails = csv.reader(f, delimiter=';')
                for info in emails:
                    name = info[1]
                    email = info[2]
                    grade = info[3]
                    session = info[4]
                    self.people[email] = {'name': name, 'grade': grade, 'session': session}


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
        self.photo = 'logo.png'

    def _login(self):
        """
            Login on server
        """
        self._server.login(self._from_email, "terceiroa")

    def send(self, **kwargs):
        """
            Send email to_email
        """
        data = {'name': name.title(),
                'hour': hour,
                'session': session,
                'to_email': to_email}
        img = MIMEImage(open('logo.png').read())
        img.add_header('Content-ID', '<{}>'.format(self.photo))
        self.psswd = randint(1000, 9999)
        self.content = """
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
  <head>
    <link rel="stylesheet" type="text/css" href="css/app.css">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Ingresso secreto</title>
    <!-- <style> -->
  </head>
  <body>
    <span class="preheader"></span>
    <table class="body">
      <tr>
        <td class="center" align="center" valign="top">
          <center data-parsed="">

            <table align="center" class="container header float-center"><tbody><tr><td>
              <table class="row"><tbody><tr>
                <th class="small-12 large-12 columns first last"><table><tr><th>
                  <h1 class="text-center">Convite para exposição de Arte</h1>

                  <center data-parsed="">
                    <table align="center" class="menu text-center float-center"><tr><td><table><tr>
                      <th class="menu-item float-center">Feito com &hearts; por todos nós do 3ºA</th>
                    </tr></table></td></tr></table>
                  </center>

                </th>
<th class="expander"></th></tr></table></th>
              </tr></tbody></table>
            </td></tr></tbody></table>

            <table align="center" class="container body-border float-center"><tbody><tr><td>
              <table class="row"><tbody><tr>
                <th class="small-12 large-12 columns first last"><table><tr><th>

                  <table class="spacer"><tbody><tr><td height="32px" style="font-size:32px;line-height:32px;">&#xA0;</td></tr></tbody></table>

                  <center data-parsed="">
                    <img src="cid:%s" width="200" height="200" align="center" class="float-center">
                  </center>
                  <table class="spacer"><tbody><tr><td height="16px" style="font-size:16px;line-height:16px;">&#xA0;</td></tr></tbody></table>

                  <h4>Obrigado por se inscrever, %s!</h4>
                  <p>Estamos lembrando-o que ocorrerá a apresentação no dia 04/12 disponível para você na %sª sessão à partir das %s no seguinte local: Sala 7 de Educação Física.</p>
                  <p>Sua senha para entrada no dia do evento é: %d</p>
                  <center data-parsed="">
                    <table align="center" class="menu float-center"><tr><td><table><tr>
                      <th class="menu-item float-center"><a href="http://pontodevista3a.myartsonline.com/index.php#edital">Confira o edital</a></th>
                      <th class="menu-item float-center"><a href="https://www.instagram.com/vistapontosde/">Instagram do evento</a></th>
                    </tr></table></td></tr></table>
                  </center>

                </th>
<th class="expander"></th></tr></table></th>
              </tr></tbody></table>

              <table class="spacer"><tbody><tr><td height="16px" style="font-size:16px;line-height:16px;">&#xA0;</td></tr></tbody></table>
            </td></tr></tbody></table>

          </center>
        </td>
      </tr>
    </table>
    <!-- prevent Gmail on iOS font size manipulation -->
   <div style="display:none; white-space:nowrap; font:15px courier; line-height:0;"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </div>
  </body>
</html>
        """ % (self.photo, data['name'], data['session'], data['hour'], self.psswd)
        self.text=  MIMEText(self.content, 'html')
        self.message['To'] = data['to_email']
        self.message.attach(self.text)
        self.message.attach(img)
        result = self._server.sendmail(self._from_email, data['to_email'], self.message.as_string())
        print 'Email enviado!'
        self._server.quit()
        return self.psswd

sessions = {'1': '9:15',
            '2': '11:10',
            '3': '11:40',
            '4': '12:20',
            '5': '13:50',
            '6': '14:40'}


filer = Filer()
filer.load_many()
people = filer.people
emails = filer.people.keys()
log = {}


# Gmail sender
for to_email in emails:
    sender = Sender()
    name = people.get(to_email)['name']
    grade = people.get(to_email)['grade']
    session = people.get(to_email)['session']
    hour = sessions.get(session)
    psswd = sender.send(to_email=to_email, name=name, session=session, hour=hour)
    log[name] = {'email': to_email, 'sessão': session, 'hora': hour, 'senha': psswd}
    with open('{}_sended_prof.csv'.format(session), 'a+') as f:
      f.write('{},{},{}\n'.format(name, grade, session))
    with open('{}_sended_staff.csv'.format(session), 'a+') as f:
      f.write('{},{},{},{}\n'.format(name, grade, session, psswd))
    print log
