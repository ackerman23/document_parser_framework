import pdfplumber

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def extract_tables_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        tables = []
        for page in pdf.pages:
            tables.extend(page.extract_tables())
    return tables
## Test the functions
pdf_text = extract_text_from_pdf("cover_letter.pdf")
print(pdf_text)

pdf_tables = extract_tables_from_pdf("cover_letter.pdf")
for table in pdf_tables:
    print(table)
