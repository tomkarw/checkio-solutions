import sendgrid
from sendgrid.helpers.mail import Email,  Mail, Content

API_KEY = 'Registrate your own key'
SUBJECT = 'Welcome'
BODY = 'Hi {}'

def send_email(email, name):
    sg = sendgrid.SendGridAPIClient(apikey=API_KEY)
    
    from_email = Email("test@example.com")
    to_email = Email(email)
    subject = "Welcome"
    content = Content("text/plain", f"Hi, {name}")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('somebody@gmail.com', 'Some Body')
    print('Done')
