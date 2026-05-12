import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

for addr in addresses:
    msg = MIMEMultipart()
    msg["From"] = os.environ["SMTP_FROM"]
    msg["To"] = addr
    msg["Subject"] = f"Task Reminder — {date_label}"
    body = f"Hi {username},\n\nHere are your tasks due within the next 3 days:\n\n{task_list}\n\nGood luck!"
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(os.environ["SMTP_FROM"], os.environ["SMTP_PASSWORD"])
        server.sendmail(os.environ["SMTP_FROM"], addr, msg.as_string())
        print(f"Email sent to {addr}!")
