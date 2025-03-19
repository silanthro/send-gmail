import os
import re
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr


def is_valid_email(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None


def send_gmail(subject: str, body: str, recipients: list[str]) -> str:
    """
    Send an email via Gmail to a list of recipients

    Args:
    - subject (str): Subject header of email
    - body (str): Contents of email
    - recipients (list[str]): Recipients as a list of email addresses

    Returns:
        A string "Email sent successfully"
    """
    sender_email_address = os.environ.get("GMAIL_ADDRESS")
    if not is_valid_email(sender_email_address):
        raise ValueError("Sender email is not a valid email address")

    sender_display_name = os.environ.get("GMAIL_DISPLAY_NAME")
    password = os.environ.get("GMAIL_PASSWORD").replace(" ", "")
    recipients = [email for email in recipients if is_valid_email(email)]

    if not recipients:
        raise ValueError("No valid recipient email addresses were supplied")

    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = formataddr((sender_display_name, sender_email_address))
    msg["To"] = ", ".join(recipients)
    msg.attach(MIMEText(body, "plain"))

    context = ssl.create_default_context()

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp_server:
        smtp_server.ehlo()
        smtp_server.starttls(context=context)
        smtp_server.ehlo()
        smtp_server.login(sender_email_address, password)
        smtp_server.sendmail(
            from_addr=sender_email_address,
            to_addrs=recipients,
            msg=msg.as_string(),
        )

    return "Email sent successfully"
