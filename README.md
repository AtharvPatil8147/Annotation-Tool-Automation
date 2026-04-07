# 🧠 Language Dialect Annotation Automation Tool

This project automates the process of submitting language annotation tasks on the DAT (Dialect Annotation Tool) platform.

It is designed to speed up repetitive annotation workflows by combining:

* CSV-based data input
* Browser automation using Playwright
* Secure credential handling using environment variables

---

## 🚀 Features

* 🔐 Automated login using credentials from `.env`
* 📄 Bulk annotation submission using CSV files
* 🌐 Full browser automation with Playwright
* ⏱️ Human-like delays to avoid detection
* 🧩 Modular and easy to extend

---

## 📁 Project Structure

```
project/
│
├── script.py              # Main automation script
├── data.csv               # Annotation data (Source, Annotated, English)
├── .env                   # Credentials (NOT pushed to GitHub)
├── .env.example           # Sample env file
├── .gitignore             # Ignore sensitive files
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

Then install Playwright browsers:

```bash
playwright install
```

---

### 3️⃣ Setup environment variables

Create a `.env` file:

```
EMAIL=your_email_here
PASSWORD=your_password_here
```

---

### 4️⃣ Prepare your data

Create `data.csv`:

```
Source,Annotated,English
काय करतोयस तू?,तू काय करत आहेस?,What are you doing?
```

---

### 5️⃣ Run the script

```bash
python script.py
```

---

## ⚠️ Important Notes

* Do NOT upload your `.env` file to GitHub
* Add delays to avoid being flagged as a bot
* Review data before submission for accuracy

---

## 🛠️ Technologies Used

* Python
* Playwright
* CSV
* dotenv

---

## 🚀 Future Improvements

* Resume from last submission
* GUI interface
* Multi-account support
* AI-based data generation

---

## 👨‍💻 Author

Atharv Patil

---

## ⭐ If you found this useful

Give this repo a star ⭐
