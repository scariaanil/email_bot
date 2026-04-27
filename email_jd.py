import re


def extract_job_details(raw_post_text):
    # Regex to find standard and obfuscated emails
    EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+(?:\s*\[at\]\s*|\s*@\s*|\s*\(at\)\s*)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    # 1. Extract Email
    emails = re.findall(EMAIL_REGEX, raw_post_text)

    # Clean the email format if found
    clean_email = None
    if emails:
        clean_email = (
            emails[0]
            .replace(" [at] ", "@")
            .replace("[at]", "@")
            .replace("(at)", "@")
            .strip()
        )

    # 2. Extract Job Description (JD)
    # We strip the email out of the text to isolate the description
    jd_content = raw_post_text

    jd_content = jd_content.replace("...see more", "").replace("\n\n", "\n").strip()

    return {"email": clean_email, "job_description": jd_content}
