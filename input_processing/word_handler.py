from docx import Document

def extract_text_from_word(docx_path):
    doc = Document(docx_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text


## Test the function
'''word_text = extract_text_from_word("J_CV.docx")
print(word_text)'''