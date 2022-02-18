import smtplib
import ssl
from email.message import EmailMessage
import os
import mimetypes
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie


fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

report = SimpleDocTemplate("./report.pdf")
styles = getSampleStyleSheet()

report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])

table_data = []
for k, v in fruit.items():
    table_data.append([k, v])
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

report_pie = Pie(width=3, height=3)
report_pie.data = []
report_pie.labels = []
for fruit_name in fruit.keys():
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

report_chart = Drawing()
report_chart.add(report_pie)

report.build([report_title, report_table, report_chart])

message = EmailMessage()
sender_email = "bvh.stonks@gmail.com"
password = "Benjam!n1122334455"
reciever_email = "bvh.stonks@gmail.com"
message["From"] = sender_email
message["To"] = reciever_email
message["Subject"] = "This mail has a pdf attachment"
body = "body"
message.set_content(body)

attachment_path = "./report.pdf"
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

with smtplib.SMTP_SSL("smtp.gmail.com", context=context)as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, reciever_email, str(message))