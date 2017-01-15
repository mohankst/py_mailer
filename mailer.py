import smtplib

# email server credentials
smtp_server = "smtp.gmail.com"
smtp_port = "587"
from_email = "mohan.kst.hp@gmail.com"

# defining a dictionary to contain all recever's data

recevers = {}

# check for the mailing list file
try:
    email_file = open('mailids.txt', 'r') #open the file mailids.txt for geeting email list

    # Geeting every single email address and name
    for line in email_file:
        (email, name) = line.split(',')
        recevers[email] = name.strip()

except FileNotFoundError as err:
    print (str(err) + ". So create it")

# check for the email body file
try:
    email_body_file = open('mailbody.txt', 'rt') #open the file mailbody.txt for geeting the content
    email_content = email_body_file.read() # read the entire file into a string variable

except FileNotFoundError as err:
    print (str(err) + ". Please create the file and put your email body in there")

def send_emails(emails, content):
    # connect to the smtp server
    server = smtplib.SMTP (smtp_server, smtp_port)

    # start TLS encription
    server.starttls()

    # email login
    password = input("What is your password?")
    server.login(from_email, password)

    email_subject = input("what's the subject")

    # send to entire email list
    for to_email, name in emails.items():
        message = 'subject:' + email_subject + '\n'
        message += 'Dear Mr ' + name + '!\n\n'
        message += content
        server.sendmail(from_email, to_email, content)

    server.quit()

def main():
    emails = recevers
    content = email_content
    send_emails(emails, content)

main()