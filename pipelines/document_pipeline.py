import sys
import os

# Add the parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from input_processing import (
    pdf_handler,
    word_handler,
)
from nlp import (
    summarizer,
    keyword_extractor,
)

def process_pdf(pdf_path):
    text = pdf_handler.extract_text_from_pdf(pdf_path)
    summary = summarizer.summarize_text(text)
    keywords = keyword_extractor.extract_keywords(text)
    tables = pdf_handler.extract_tables_from_pdf(pdf_path)
    
    return {
        #"text": text,
        "summary": summary,
        #"keywords": keywords,
        #"tables": tables
    }

def process_word(docx_path):
    text = word_handler.extract_text_from_word(docx_path)
    summary = summarizer.summarize_text(text)
    keywords = keyword_extractor.extract_keywords(text)
    
    return {
        #"text": text,
        "summary": summary,
        #"keywords": keywords
    }
    
## Test the function
result = process_pdf("/Users/jihadgarti/Desktop/github-path/document_parser_framework/cover_letter.pdf")
print(result)

