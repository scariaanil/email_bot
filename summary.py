import os

from dotenv import load_dotenv

from email_jd import extract_job_details
from jd_reader import get_job_description

load_dotenv()
details = os.getenv("details")

summary = """Professional Summary:
    Performance-driven Quality Analyst with 5.5 years of expertise specializing in high-impact Web and Mobile platforms. I bridge the gap between rigorous manual exploratory testing and efficient automation using Java, Selenium, and Appium, while actively expanding my toolkit with Python Playwright and ETL testing. A dedicated Full-Stack QA and AI-savvy tester, I excel at optimizing app stability through advanced performance profiling and leveraging AI tools to enhance testing efficiency in fast-paced Agile environments.

Core Competencies:
    Automation Engineering (Web & Mobile): Hands-on experience building and maintaining robust frameworks using Java, Selenium, and Appium.Next-Gen Automation: Currently practicing Python with Playwright for modern, fast, and reliable web automation.Data & Backend Integrity: Proficient in REST API testing (Postman) and currently building expertise in ETL testing to ensure data accuracy across complex pipelines.AI Tool Integration: Familiar with leveraging AI tools to accelerate test case generation, documentation, and debugging workflows.Performance & Stability Profiling: Specialized in UI performance monitoring, tracking Frames Per Second (FPS), and identifying memory leaks to prevent app crashes.Mobile Debugging Specialist: Advanced usage of Android Studio, Chrome DevTools, and ADB for deep-dive debugging and hardware compatibility testing.Agile & Full-Stack QA: Expert in the complete STLC, participating in sprint planning and bug triage via Jira to deliver end-to-end product excellence.Infrastructure Support: Proven track record in stabilizing complex transitions, such as Server-Side Rendering (SSR) migrations."""


post = get_job_description()

result = extract_job_details(post)
job_desc = result["job_description"]
print(f"Job Description: {job_desc}")


relevance_prompt = f"""
    Compare the following Job Description (JD) to my Professional Summary.

    MY SUMMARY:
    {summary}

    JOB DESCRIPTION:
    {job_desc}

    TASK:
    Rate the match from 0 to 100 based on how well my skills meet the requirements.
    Return ONLY the numerical integer value. Do not include any text, reasoning, or symbols.
    """


email_prompt = f"""
Please write a professional, engaging email body for a job application.
I am applying for the role described below.
Make sure to explicitly mention that my CV/resume is attached to the email for their review.
Keep the tone confident but polite, and highlight how my skills align with the requirements.

CRITICAL INSTRUCTIONS:
1. DO NOT use any Markdown formatting. Do not use **asterisks** for bolding. Use 100% plain text.
2. Do not use placeholders like [Your Name]. Use the real details provided below to sign off the email.
3. The very FIRST line of your response MUST start with "Subject: " followed by a strong subject line.
4. Note down the Current and Expected CTC at the end of the email, Only id it is asked in the job description
5. Preferedd location should always be mentioned as Bangalore, Chennai, If it ia available in the job description, If there is no mention of preferred location, do not add it.

Here is the job description and personal details to use:
{job_desc} {details}
"""
