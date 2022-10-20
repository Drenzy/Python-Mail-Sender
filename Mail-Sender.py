from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'dhartwich650@gmail.com'
email_passwrd = 'ccorattysbtcouxm'

email_reciever = 'demonlazze7@gmail.com'

subject = "Hej"

body = """
jeg har været inde på jeres hjemmeside og læse lidt om jer og jeres arbejde indenfor software design. Det er noget som jeg selv brænder meget for.
Hermed sender jeg min ansøgning om en elevplads som programmør samt mit CV. Jeg håber i vil tage min ansøgning i overvejelse.
Håber i har en rigtig god dag.

Mvh Daniel Nikolaj Hartwich
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)
context = ssl.create_default_context()


with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_passwrd)
    smtp.sendmail(email_sender,email_reciever,em.as_string())
# app passw0rd ccorattysbtcouxm
