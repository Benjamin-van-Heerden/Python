from email.message import EmailMessage
import os
import mimetypes
import smtplib

message = EmailMessage()
sender = "benjaminvh1997@gmail.com"
recipient = "bvh.stonks@gmail.com"

message["From"] = sender
message["To"] = recipient

message["Subject"] = f"Greetings from {sender} to {recipient}"

body = "Test"
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

mail_server = smtplib.SMTP("localhost")