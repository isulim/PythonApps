from email.mime.text import MIMEText
from smtplib import SMTP


def send_email(email, height, avg_height, total_users):
    from_email = "ajdziajpython@gmail.com"
    from_password = "AjdziajPython123"
    to_email = email

    subject = "Height data"
    message = """Hey there,<br>
                 your height is <strong>{}</strong> cm.<br>
                 Average height of <strong>{}</strong> people is 
                 <strong>{}</strong> cm.<br>
                 Thanks for participating!
              """.format(height, total_users, avg_height)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)