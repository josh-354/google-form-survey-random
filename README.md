# Canva Slides to PDF

This Python script automates capturing **Canva presentation slides** and exporting them into a **single PDF file**.  
It uses **Selenium** to control Chrome, takes screenshots of each slide, and then compiles them into an **A4-sized PDF** stretched to fill the page (no white bars, no cropping).  

---

## 🚀 Features
- Automatically captures all slides from a Canva presentation
- Navigates slides using Selenium & Chrome
- Saves each slide as a PNG image
- Combines slides into a single PDF
- Output PDF has **no borders or cropping**

---

## 📦 Requirements
- **Python 3.8+**
- Install dependencies:
  ```bash
  pip install pillow fpdf selenium
Google Chrome installed

ChromeDriver installed (must match your Chrome version)

Download ChromeDriver

Or install automatically with:

bash
Copy code
pip install webdriver-manager
⚙️ What to Change in the Code
Open the script and update these variables:

python
Copy code
# Canva presentation link
CANVA_URL = "https://www.canva.com/design/XXXX/view"

# Number of slides in your Canva presentation
NUM_SLIDES = 64  

# Time (in seconds) to wait before capturing the next slide
WAIT_TIME = 0.5  

# Folder where screenshots and PDF will be saved
OUTPUT_FOLDER = "canva_slides" 