import sendgrid
import os
import base64
from uuid import uuid4
import urllib.request as urllib
from mimetypes import guess_type
from sendgrid.helpers.mail import Email, Content, Mail, Attachment


FROM_EMAIL = "info@grepsr.com"
TO_EMAIL = "chapagainmanoj35@gmail.com"

def new_attachment(file_path, content_type, filename, content_id):
    with open(file_path,'rb') as f:
        data = f.read()
        f.close()
    encoded = base64.b64encode(data).decode()
    attachment = Attachment()
    attachment.content = encoded
    attachment.type = content_type
    attachment.filename = filename
    attachment.disposition = "attachment"
    attachment.content_id = content_id

    return attachment

def send_mail(file_path,title):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email(FROM_EMAIL)
    to_email = Email(TO_EMAIL)

    content = Content("text/html","Output Attachments: {}".format(title))
    subject = "QUID LAB: Outputs"

    with open(file_path,'rb') as f:
        data = f.read()
        f.close()
    encoded = base64.b64encode(data).decode()
    attachment = Attachment()
    attachment.content = encoded
    attachment.type = guess_type(file_path)[0] or 'application/octet-stream'
    attachment.filename = file_path.split('/')[-1]
    attachment.disposition = "attachment"
    attachment.content_id = str(uuid4())

    mail = Mail(from_email, subject, to_email, content)
    mail.add_attachment(attachment)
    try:
        response = sg.client.mail.send.post(request_body=mail.get())
        if response.status_code == 202:
            print("Sent Successfully")
        else:
            print("ERROR: %d",response.status_code)
        print(response.status_code)
    except urllib.HTTPError as e:
        return e.read()
