import fitz  # PyMuPDF

pdf_path = "sample_paper.pdf"

doc = fitz.open(pdf_path)
text = ""
for page in doc:
    text += page.get_text()

with open("extracted_text.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("✅ PDF text saved to extracted_text.txt")
