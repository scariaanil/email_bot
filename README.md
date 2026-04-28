# 🚀 AI-Powered Job Application Email Bot

An automated Python pipeline that reads job descriptions, uses the **Google Gemini API** to draft highly tailored application emails, and automatically sends them to recruiters with a resume attached. This bot is designed to run locally from your development environment.

## ✨ Features
* **AI Email Generation:** Leverages Gemini 2.5 Flash to write contextual, professional emails matching your skills to the specific Job Description.
* **Resilience & Error Handling:** Built-in modular safe file reading and API connection management.
* **Automated Email Delivery:** Uses Python's native `smtplib` to securely send emails via Gmail.
* **Smart Attachments:** Automatically attaches your PDF resume to the outgoing email.
* **BCC Support:** Sends a hidden copy to your personal email for record-keeping.

## 🛠️ Tech Stack
* **Language:** Python 3.12.10
* **AI Model:** Google Gemini API (`google-generativeai`)
* **Email Protocol:** SMTP (`smtplib`, `email.message`)
* **Environment Management:** `python-dotenv`

## ⚙️ Prerequisites
Before running this project, you will need:
1. Python installed on your machine.
2. A **Gemini API Key** (Get one from [Google AI Studio](https://aistudio.google.com/)).
3. A **Google App Password** for your Gmail account (Standard Gmail passwords will not work for SMTP. Generate an App Password in your Google Account Security settings).

## 🚀 Setup & Installation

**1. Clone the repository:**
```bash
git clone [https://github.com/scariaanil/email_bot.git](https://github.com/scariaanil/email_bot.git)
# Make sure to navigate to your project root, E:\Zed Playwright Project\Application
cd Application

2. Set up your virtual environment:

3. Install dependencies:Bash pip install google-generativeai python-dotenv

4. Environment Variables Setup:Create a file named .env in the root directory and add your credentials. (Note: This file is already ignored by Git for security).Code snippet API_KEY_GEMINI="your_gemini_api_key_here"
EMAIL_SENDER="your_gmail_address@gmail.com"
EMAIL_APP_PASSWORD="your_16_digit_google_app_password"


📁 Project Structure (Verified from Local Repo)This diagram shows the correct, modularized structure of the project as of image_0.png.PlaintextApplication/ (Project Root)
│
├── Resume/                  # Folder for storing target resume files
│   └── QA_5yrs_Scaria_Anil.pdf # Your specific resume file
│
├── application/             # (Python Venv, git ignored)
│
├── .env                     # Secrets and API keys (Not tracked by Git)
├── .gitignore               # Configures files and folders to ignore
│
├── check_relevance.py       # Main script to check JD relevance
├── draft_email.py           # Main entry point (AI generation + execution)
├── email_jd.py               # Utility to extract/format JD text details
├── interface.py             # User interface or API connection layer
├── jd.txt                   # Paste target Job Descriptions here
├── jd_reader.py             # Utility to safely read multi-line text files
├── key.py                   # User-added key management (Ensure this is secure!)
├── send_email.py            # Email protocol (SMTP) module
└── summary.py               # AI prompt engineer (Generates the final drafted text)

🔐 Security Warning (CRITICAL)Your .env file and Resume/*.pdf files are already being ignored by .gitignore.

📖 How to UseUpdate your details: Open draft_email.py and ensure the paths to your resume and recruiter details are updated. Add the Job Description: Paste the full target Job Description into jd.txt.

Run the bot: python interface.py

WorkFlow

[ START: interface.py ]
      │
      ├─► 1. jd_reader.py
      │      └─► Reads `jd.txt`
      │      └─► [FAIL] ──► If empty/missing, PRINT error & EXIT.
      │      └─► [SUCCESS] ──► Returns raw JD string.
      │
      ├─► 2. email_jd.py
      │      └─► Scans raw JD for regex email patterns.
      │      └─► Returns Dictionary: {email, job_description}.
      │
      ├─► 3. summary.py (Prompt Generation)
      │      └─► Injects JD into `relevance_prompt`.
      │
      ├─► 4. ai_response.py (Scoring)
      │      └─► Sends prompt to Gemini 2.5 Flash-Lite.
      │      └─► Extracts integer from response using regex.
      │      └─► Returns Score (0-100).
      │
      ├─► 5. DECISION GATE (interface.py)
      │      ├─► [Score < 70] ──► PRINT "Not relevant" & EXIT.
      │      │
      │      └─► [Score >= 70] 
      │             │
      │             ├─► WAIT 60 SECONDS (API Cooldown).
      │             │
      │             ├─► 6. summary.py (Prompt Generation)
      │             │      └─► Injects JD and .env details into `email_prompt`.
      │             │
      │             ├─► 7. ai_response.py (Drafting)
      │             │      └─► Sends prompt to Gemini.
      │             │      └─► Returns clean drafted text.
      │             │
      │             └─► 8. send_email.py
      │                    ├─► Locates local PDF CV.
      │                    ├─► Parses drafted text for Subject/Body.
      │                    ├─► Connects to smtp.gmail.com.
      │                    └─► Sends application to Recruiter.
      │
[ END: Script Terminates Successfully ]


🤝 Contributing
Feel free to fork this repository, submit pull requests, or open issues to suggest improvements!
