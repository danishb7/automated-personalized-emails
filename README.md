# Automated Personalized Email Sender (Python Script)

This project automates the task of sending **personalized, one-on-one emails** to multiple people using Python. Each recipient gets a custom message with their name in the body and their email in the "To" field — **no BCCs**, no mass sends.

---


## 🔧 Requirements

Install dependencies with:

```pip install -r requirements.txt```


##  .env File

Create a file named `.env` in the project root:

SMTP\_USER=your\_email@gmail.com

SMTP\_PASS=your\_16\_char\_app\_password


> Get your App Password by:

> - Enabling 2-Step Verification

> - Visiting: https://myaccount.google.com/apppasswords

> - Generating a "Mail" app password (you'll get a 16-character code — **no spaces!**)

---

## recipients.csv Format

name,email

Danish Bhatkar,danishb@company.com

Danish Bhatkarr,danishb7@startup.com

Common Issues & Fixes
------------------------

### Authentication Error (SMTPAuthenticationError)

*   Cause: Using normal password instead of App Password
    
*   Fix:
    
    *   Enable 2-Step Verification: https://myaccount.google.com/security
        
    *   Generate App Password: https://myaccount.google.com/apppasswords
        
    *   Paste that password into your .env file (no spaces)
        

### KeyError: 'name'

*   Cause: CSV exported with invisible BOM or header typo
    
*   Fix:
    
    *   Ensure the first line of CSV is: name,email
        
    *   Use encoding="utf-8-sig" when opening the file
        

> 🚫 Never commit .env to GitHub — it contains your private credentials.

Author
---------

**Danish Bhatkar**

📍 Computer Science Grad @ Clemson University

🌐 GitHub: [danishb7](https://github.com/danishb7)

💼 LinkedIn: [danish-bhatkar](https://www.linkedin.com/in/danish-bhatkar)

📬 Wanna Try It?
----------------

Just run:

```python script.py```

...and watch personalized emails fly out ✈️


### ⚠️ Things to remember..

* Gmail has some restrictions on the number of emails you can send daily as well as hourly. Make sure you keep your recipients' list short!

* You can implement batch processing of emails if your list is long (say 70-100), and implement it in this code.

* You can also add a sleep timer in the loop, so it waits for a few seconds before sending out the next email!
