# 📘 PDF to Audiobook Converter (Python)

Convert any PDF book into an audiobook using Python.  
This project reads text from a PDF file and converts it into speech using a text-to-speech engine.

---

## 🚀 Features

- 📄 Reads text from PDF files
- 🔊 Converts text into clear audio narration
- 📑 Skips empty pages automatically
- 🎧 Adjustable voice and speech rate
- 🧠 Beginner-friendly Python project
- 💻 Works on Windows, macOS, and Linux

---

## 🛠️ Technologies Used

- Python
- PyPDF2
- pyttsx3 (Text to Speech)
- Tkinter (File selection)
- VS Code
- Git & GitHub

---

## 📂 Project Structure

```

python-pdf-to-audiobook/
│
├── audiobook.py        # Main Python script
├── README.md           # Project documentation
├── requirements.txt    # Required Python packages
└── sample.pdf          # (Optional) Sample PDF for testing

````

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/ABHINASH1204/python-pdf-to-audiobook.git
cd python-pdf-to-audiobook
````

### 2️⃣ Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it:

* **Windows**

```bash
venv\Scripts\activate
```

* **macOS / Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python audiobook.py
```

* A file dialog will open
* Select a PDF file
* The program will start reading pages aloud
* Empty pages are skipped automatically

---

## ⚙️ Customization

You can change:

* 🔉 Voice (male/female)
* ⏩ Speech rate
* 📄 Start and end page numbers

Inside the code:

```python
speaker.setProperty('rate', 180)
speaker.setProperty('voice', voices[1].id)
```

---

## 🧪 Example Output

```text
📖 Reading page 1
📖 Reading page 2
⚠️ Skipped empty page 3
✅ Audiobook finished successfully!
```

---

## 🧠 Learning Outcomes

* Working with PDFs in Python
* Text preprocessing
* Text-to-Speech automation
* Git & GitHub workflow
* Building real-world Python projects

---

## 📌 Future Improvements

* Save audio as MP3/WAV files
* GUI interface
* Language selection
* Chapter-wise audio output

---

## 👤 Author

**Abhinash Bishoi**
📌 GitHub: [https://github.com/ABHINASH1204](https://github.com/ABHINASH1204)

---

## ⭐ Support

If you like this project, don’t forget to ⭐ star the repository!

```

---

## 🔥 Next small steps (recommended)
I can also:
- Create `requirements.txt`
- Improve code structure
- Add GUI version
- Make this project **resume-perfect**
- Suggest your **next Python/Data Analytics project**

Just say the word 😄
```
