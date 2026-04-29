import time

from application_logger import log_application
from check_relevance import get_relevance_score
from draft_email import draft_email
from email_jd import extract_job_details
from send_email import send_application_email
from summary import post

details = extract_job_details(post)
hr_email = details.get("email", "No_Email_Found")
description = details.get("job_description", "No JD Found")
print(f"Job Description: {description} \n\n Recruiter Email: {hr_email}")

try:
    relevance_score = get_relevance_score()
    if relevance_score is not None:
        if relevance_score >= 70:
            print("\nWaiting For a Minute to aviod Gemini API overloading....! ")
            time.sleep(60)
            print("\nResuming Execution: Proceeding to draft Email...!")
            email_text = draft_email()
            print(f"Email body: {email_text}\n\n")
            try:
                send_application_email(email_text, hr_email)
                log_application(hr_email, "Sent")

            except Exception as e:
                print(f"Failed to send the email: {e}")
                log_application(hr_email, "Not sent")
        else:
            print("Job is not relevant to your profile")
            log_application(hr_email, "Not eligible")
    else:
        print("There was an issue fetching relevance score")
        log_application(hr_email, "Not sent")
except Exception as e:
    print(f"A critical error occurred during the process: {e}")
    log_application(hr_email, "Not sent")
