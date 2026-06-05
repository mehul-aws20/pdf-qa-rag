
from PyPDF2 import PdfReader

def load_pdfs(files):
    chunks = []
    for file in files:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        for i in range(0, len(text), 500):
            chunks.append(text[i:i+500])
    return chunks
