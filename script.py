import os, csv, smtplib, time
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base  import MIMEBase
from email import encoders

load_dotenv()
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")

# print("SMTP_USER:", SMTP_USER)
# print("SMTP_PASS:", SMTP_PASS)


# 1) connect & login
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SMTP_USER, SMTP_PASS)



with open("recipients.csv") as f:
    for row in csv.DictReader(f):
        name = row["name"]
        to_addr = row["email"]

        # 2) build a multipart message
        msg = MIMEMultipart("alternative")
        msg["From"] = SMTP_USER
        msg["To"]   = to_addr
        msg["Subject"] = f"Quick Intro – {name}"

        # 3) plain-text part
        text = f"""\
Hey {name},

I’m DB, just testing this script.

Cheers,
DB
"""
        part1 = MIMEText(text, "plain")

        # 4) HTML fallback
        html = f"""\
<html>
  <body>
    <p>Hey {name},<br><br>
       I’m <b>DB</b>, just testing this script<br><br>
       Cheers,<br>
       DB
    </p>
  </body>
</html>
"""
        part2 = MIMEText(html, "html")

        # attach both
        msg.attach(part1)
        msg.attach(part2)

        # 5) optional attachment (resume.pdf)
        filename = "resume.pdf"
        if os.path.exists(filename):
            with open(filename, "rb") as attach:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attach.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={filename}",
            )
            msg.attach(part)

        # 6) send + rate-limit
        server.send_message(msg)
        time.sleep(2)  # chill for 2s so you don’t hit spam limits

server.quit()
