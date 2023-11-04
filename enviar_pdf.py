import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

import os
from dotenv import load_dotenv

load_dotenv()

APP_PASS = os.getenv("APP_PASS")

# Gmail account settings
sender_email = "javierrojas14.jr@gmail.com"
sender_password = APP_PASS  # Use the App Password you generated
receiver_email = "javierrojas14.jr@gmail.com"
subject = "Reporte pesos"

# Create a message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Email body
body = "Hello, this is your PDF file."
message.attach(MIMEText(body, "plain"))

# Attach the PDF file
pdf_file_path = "reporte.pdf"
with open(pdf_file_path, "rb") as pdf_file:
    pdf_attach = MIMEApplication(pdf_file.read(), _subtype="pdf")
    pdf_attach.add_header("Content-Disposition", "attachment", filename="your_pdf.pdf")
    message.attach(pdf_attach)

# Send the email using SMTP
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Email could not be sent. Error: {str(e)}")
