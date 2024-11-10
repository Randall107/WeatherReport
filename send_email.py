from email.message import EmailMessage
from typing import List
import ssl
import smtplib
class email:
    def send(email_list: List[str], content):
        sender = "randall107hasalreadybeentaken@gmail.com"
        password = ""
        subject = "Today's Weather Report"
        body = f"""
        {content}
        """
        em = EmailMessage()
        em['From'] = sender
        em['Subject'] = subject
        em.set_content(body)
        i = 0
        while i < len(email_list):
            receiver = email_list[i]
            em['To'] = receiver
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(sender, password)
                smtp.sendmail(sender, receiver, em.as_string())
            del em['To']
            i = i + 1
