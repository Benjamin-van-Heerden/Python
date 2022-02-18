import smtplib, ssl
from email.message import EmailMessage
import mimetypes
import os

port = 465
password = "Benjam!n1122334455"
sender_email = "bvh.stonks@gmail.com"
receiver_email = "bvh.stonks@gmail.com"
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "This is a more structured test email"
body = "This is the body of the email"
message.set_content(body)

attachment_path = "../week1/example_images/coding.png"
attachment_filename = os.path.join(attachment_path)

mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split("/", 1)

with open(attachment_path, "rb") as ap:
    message.add_attachment(
        ap.read(),
        maintype = mime_type, 
        subtype = mime_subtype,
        filename = attachment_filename
    )


context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, str(message))