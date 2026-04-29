import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
PERSONAL_EMAIL = os.getenv("PERSONAL_EMAIL")


def send_application_email(email_text, recruiter_email):
    cv_file_path = os.path.join("Resume", "QA_5yrs_Scaria_Anil.pdf")
    # 1. Parse the Subject and the Body
    lines = email_text.strip().split("\n")
    subject = "Job Application"  # Fallback subject just in case
    body_lines = []

    for line in lines:
        # Check if the line starts with "Subject:" (case-insensitive)
        if line.lower().startswith("subject:"):
            # Split at the first colon and grab the actual subject text
            subject = line.split(":", 1)[1].strip()
        else:
            # Everything else goes into the body
            body_lines.append(line)

    # Rejoin the remaining lines to create the clean email body
    email_body = "\n".join(body_lines).strip()

    if not SENDER_EMAIL or not EMAIL_PASSWORD:
        print("Error: Missing SENDER_EMAIL or EMAIL_PASSWORD in .env file.")
        return

    print(f"-> Extracted Subject: {subject}")
    print("-> Preparing email and attaching CV...")

    # 3. Create the Email Container
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = recruiter_email
    msg.set_content(email_body)
    if PERSONAL_EMAIL:
        msg["Bcc"] = PERSONAL_EMAIL

    safe_attachment_name = os.path.basename(cv_file_path)

    # 4. Attach the CV
    try:
        with open(cv_file_path, "rb") as f:
            pdf_data = f.read()

        msg.add_attachment(
            pdf_data,
            maintype="application",
            subtype="pdf",
            filename=safe_attachment_name,
        )
        print("-> CV attached successfully!")
    except FileNotFoundError:
        print(f"Error: Could not find the file '{cv_file_path}'. Email not sent.")
        return

    # 5. Send the Email
    print("-> Sending email via Gmail SMTP...")
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, EMAIL_PASSWORD)
            server.send_message(msg)
        print("\nSuccess! Your application has been sent.")
    except Exception as e:
        print(f"\nFailed to send email. Error: {e}")
