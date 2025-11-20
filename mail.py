from dataclasses import dataclass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import ssl
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class TechIdeiasMail:
    sender_email: str
    password: str

    def login(self, email_address, email_password):
        self.sender_email = email_address
        self.password = email_password

    def send_email(self, subject, body, to_email):
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))
        
        # Set up the secure SSL context
        context = ssl.create_default_context()
        
        try:
            # Connect to the mail server using TLS encryption
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls(context=context)
                server.login(self.sender_email, self.password)
                text = msg.as_string()
                server.sendmail(self.sender_email, to_email, text)
            
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error: {e}")

    def send_html_email(self, subject, body, to_email):
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Attach the HTML body
        msg.attach(MIMEText(body, 'html'))
        
        context = ssl.create_default_context()
        
        try:
            # Connect to the mail server and send the email
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls(context=context)
                server.login(self.sender_email, self.password)
                text = msg.as_string()
                server.sendmail(self.sender_email, to_email, text)
            
            print("HTML email sent successfully!")
        except Exception as e:
            print(f"Error: {e}")

    def send_email_with_attachment(self, subject, body, to_email, attachment_path):
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))
        
        # Open and attach the file
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={attachment_path.split('/')[-1]}",
            )
            msg.attach(part)
        
        context = ssl.create_default_context()
        
        try:
            # Connect to the mail server and send the email
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls(context=context)
                server.login(self.sender_email, self.password)
                text = msg.as_string()
                server.sendmail(self.sender_email, to_email, text)
            
            print("Email with attachment sent successfully!")
        except Exception as e:
            print(f"Error: {e}")