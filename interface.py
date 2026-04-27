import time

from check_relevance import get_relevance_score
from draft_email import draft_email
from email_jd import extract_job_details
from send_email import send_application_email
from summary import post

details = extract_job_details(post)
print(
    f"Job Description: {details['job_description']} \n\n Recruiter Email: {details['email']}"
)
relevance_score = get_relevance_score()
if relevance_score is not None:
    if relevance_score >= 70:
        print("\nWaiting For a Minute to aviod Gemini API overloading....! ")
        time.sleep(60)
        print("\nResuming Execution: Proceeding to draft Email...!")
        email_text = draft_email()
        print(f"Email body: {email_text}\n\n")
        send_application_email(email_text, details["email"])
    else:
        print("Job is not relevant to your profile")
else:
    print("Relevance Score is None")
