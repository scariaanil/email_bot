import time

from ai_response import get_ai_response
from email_jd import extract_job_details
from jd_reader import get_job_description
from send_email import send_application_email
from summary import get_email_prompt, get_relevance_prompt


def main():
    print("Initializing Application Bot...")

    # 1. Read and Parse JD once
    raw_jd = get_job_description()
    if not raw_jd:
        return  # Stops execution if file is missing/empty

    details = extract_job_details(raw_jd)
    job_desc = details["job_description"]
    recruiter_email = details["email"]

    print(f"Recruiter Email Found: {recruiter_email}")

    # 2. Check Relevance
    rel_prompt = get_relevance_prompt(job_desc)
    relevance_score = get_ai_response(rel_prompt, task_type="score")

    if relevance_score is not None and int(relevance_score) >= 70:
        print("\nScore is high enough. Waiting 60s to respect API rate limits...")
        time.sleep(60)

        # 3. Draft Email
        print("\nDrafting Email...")
        email_prompt = get_email_prompt(job_desc)
        email_text = get_ai_response(email_prompt, task_type="text")

        # 4. Send Email
        if email_text and recruiter_email:
            send_application_email(email_text, recruiter_email)
        else:
            print("Missing email text or recruiter email. Cannot send.")
    else:
        print(f"Job is not relevant (Score: {relevance_score}). Aborting.")


if __name__ == "__main__":
    main()
