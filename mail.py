import sendgrid
import os
import base64
import urllib.request as urllib
from sendgrid.helpers.mail import Email, Content, Mail, Attachment

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

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("info@grepsr.com")
to_email = Email("chapagainmanoj35@gmail.com")


content = Content("text/html","Output Attachments")
subject = "Testing Templates"

file_path = "output_templates/template_1.xlsx"
pdf_path = "xyz.pdf"
att1 = new_attachment(file_path,"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",'test.xlsx', "bla")
att2 = new_attachment(pdf_path,"application/pdf",'test.pdf', "bla")


mail = Mail(from_email, subject, to_email, content)
mail.add_attachment(att1)
mail.add_attachment(att2)

try:
    response = sg.client.mail.send.post(request_body=mail.get())
except urllib.HTTPError as e:
    print(e.read())
    exit()

print(response.status_code)
print(response.body)
print(response.headers)
