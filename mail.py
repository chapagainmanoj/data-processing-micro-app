import sendgrid
import os
import base64
import urllib.request as urllib
from sendgrid.helpers.mail import Email, Content, Mail, Attachment

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("info@grepsr.com")
to_email = Email("chapagainmanoj35@gmail.com")

content = Content("text/html")
file_path = "xyz.pdf"
subject = "Test ing"
with open(file_path,'rb') as f:
    data = f.read()
    f.close()
encoded = base64.b64encode(data).decode()

attachment = Attachment()
attachment.content = encoded
attachment.type = "application/pdf"
attachment.filename = "test.pdf"
attachment.disposition = "attachment"
attachment.content_id = "Example Content ID"

mail = Mail(from_email, subject, to_email, content)
mail.add_attachment(attachment)

body = mail.get()
print(body)

try:
    response = sg.client.mail.send.post(request_body=body)
except urllib.HTTPError as e:
    print(e.read())
    exit()

print(response.status_code)
print(response.body)
print(response.headers)
