import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
body = '''Informe Generat Automàticament amb Grafana.
'''
sender = 'xxx'
password = 'xxx'

receiver = 'xxx'
 
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'Grafana Report'
 
message.attach(MIMEText(body, 'plain'))
 
pdfname = '/root/go/bin/out.pdf'

# open the file in bynary
binary_pdf = open(pdfname, 'rb')
 
payload = MIMEBase('application', 'octate-stream', Name=pdfname)
# payload = MIMEBase('application', 'pdf', Name=pdfname)
payload.set_payload((binary_pdf).read())
 
# enconding the binary into base64
encoders.encode_base64(payload)
 
# add header with pdf name
payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
message.attach(payload)
 
#use gmail with port
session = smtplib.SMTP('smtp.gmail.com', 587)
 
#enable security
session.starttls()
print("Iniciant sesió") 
#login with mail_id and password
session.login(sender, password)
 
text = message.as_string()
session.sendmail(sender, receiver, text)
session.quit()
print('Mail Sent')
