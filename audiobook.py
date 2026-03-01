import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename
from tkinter import Tk

# -------------------- Hide Tk window --------------------
Tk().withdraw()

# -------------------- Select PDF --------------------
book = askopenfilename(
    title="Select a PDF file",
    filetypes=[("PDF Files", "*.pdf")]
)

if not book:
    print("❌ No file selected")
    exit()

# -------------------- Read PDF --------------------
pdfReader = PyPDF2.PdfReader(book)
total_pages = len(pdfReader.pages)

print(f"📄 Total pages found: {total_pages}")

# -------------------- Initialize TTS --------------------
speaker = pyttsx3.init()

# -------------------- Voice Setup --------------------
voices = speaker.getProperty('voices')

# Female voice (fallback safe)
try:
    speaker.setProperty('voice', voices[1].id)
    print("🎙 Female voice selected")
except:
    speaker.setProperty('voice', voices[0].id)
    print("🎙 Default voice selected")

# -------------------- Speed Control --------------------
speed_mode = "slow"   # options: slow | normal | fast

if speed_mode == "slow":
    speaker.setProperty('rate', 130)
elif speed_mode == "fast":
    speaker.setProperty('rate', 190)
else:
    speaker.setProperty('rate', 160)

# -------------------- Volume --------------------
speaker.setProperty('volume', 1.0)  # 0.0 to 1.0

# -------------------- Page Range --------------------
start_page = 0               # page index starts from 0
end_page = total_pages       # change if needed

print(f"📘 Reading pages {start_page + 1} to {end_page}")

# -------------------- Read Pages --------------------
for page_num in range(start_page, end_page):
    page = pdfReader.pages[page_num]
    text = page.extract_text()

    if text and text.strip():
        clean_text = " ".join(text.split())
        print(f"🔊 Reading page {page_num + 1}")
        speaker.say(clean_text)
    else:
        print(f"⚠ Skipped empty page {page_num + 1}")

# -------------------- Start Speaking --------------------
speaker.runAndWait()

print("✅ Audiobook finished successfully 🎧")