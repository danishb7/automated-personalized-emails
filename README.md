\# 📧 Automated Personalized Email Sender (Python Script)

This project automates the task of sending \*\*personalized, one-on-one emails\*\* to multiple recruiters using Python. Each recipient gets a custom message with their name in the body and their email in the "To" field — \*\*no BCCs\*\*, no mass sends.

\---

\## 📁 Project Structure

EmailScript/

├── script.py # Main Python script that sends the emails

├── .env # Stores your Gmail & App Password (NOT committed to GitHub)

├── resume.pdf # Resume or any other file to attach

├── recipients.csv # List of recipient names and emails

├── README.md # Project documentation

yaml

Copy

Edit

\---

\## 🔧 Requirements

Create a \`requirements.txt\` file containing:

python-dotenv

csharp

Copy

Edit

Install dependencies with:

pip install -r requirements.txt

yaml

Copy

Edit

\---

\## ⚙️ .env File

Create a file named \`.env\` in the project root:

SMTP\_USER=your\_email@gmail.com

SMTP\_PASS=your\_16\_char\_app\_password

yaml

Copy

Edit

\> 🟡 Get your App Password by:

\> - Enabling 2-Step Verification

\> - Visiting: https://myaccount.google.com/apppasswords

\> - Generating a "Mail" app password (you'll get a 16-character code — \*\*no spaces!\*\*)

\---

\## 👥 recipients.csv Format

name,email

Alice Johnson,alice.johnson@company.com

Bob Smith,bob.smith@startup.com

🧯 Common Issues & Fixes
------------------------

### 🔐 Authentication Error (SMTPAuthenticationError)

*   Cause: Using normal password instead of App Password
    
*   Fix:
    
    *   Enable 2-Step Verification: https://myaccount.google.com/security
        
    *   Generate App Password: https://myaccount.google.com/apppasswords
        
    *   Paste that password into your .env file (no spaces)
        

### 🧵 KeyError: 'name'

*   Cause: CSV exported with invisible BOM or header typo
    
*   Fix:
    
    *   Ensure the first line of CSV is: name,email
        
    *   Use encoding="utf-8-sig" when opening the file
        

🛑 .gitignore Example
---------------------

Create a .gitignore file in your repo with:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopyEdit.env  __pycache__/  *.pyc  .DS_Store   `

> 🚫 Never commit .env to GitHub — it contains your private credentials.

🙌 Author
---------

**Danish Bhatkar**📍 Computer Science Grad @ Clemson University🌐 GitHub: [danishb7](https://github.com/danishb7)💼 LinkedIn: [danish-bhatkar](https://www.linkedin.com/in/danish-bhatkar)

📬 Wanna Try It?
----------------

Just run:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   nginxCopyEditpython script.py   `

...and watch personalized recruiter emails fly out ✈️🔥
