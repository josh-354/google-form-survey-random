# 📝 Google Form Auto-Filler (Robust)

This Python script automates filling out and submitting **Google Forms** multiple times using **Selenium**.  
It randomizes answers from a set of predefined responses and can run as many submissions as you like.

---

## 🚀 Features
- Works with **Google Forms** (radio buttons, checkboxes, dropdowns, etc.)
- Randomly chooses from sample responses
- Automatically submits the form
- Optionally clicks **"Submit another response"** if available
- Built with **Selenium + webdriver-manager** (no need to manually download ChromeDriver)

---

## 📦 Requirements
- **Python 3.8+**
- **Google Chrome** installed
- Install required packages:
  ```bash
  pip install selenium webdriver-manager
⚙️ Configuration
🔗 Google Form
Update this variable in the script with your form link:

python
Copy code
FORM_URL = "https://docs.google.com/forms/d/e/XXXXX/viewform"
🔁 Number of Submissions
How many times to submit the form:

python
Copy code
NUM_SUBMISSIONS = 10   # Example: 100 for large runs