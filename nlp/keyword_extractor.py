import spacy
from pathlib import Path
import docx2txt

# Load pre-trained spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_keywords(input_text, include_pos=['NOUN', 'PROPN'], min_length=3):
    """
    Extract keywords from text based on part-of-speech tags and other criteria.
    
    Args:
        input_text: Input text or path to document
        include_pos: List of spaCy POS tags to include
        min_length: Minimum length of keywords to include
    """
    # Process the text
    doc = nlp(input_text)
    
    # Extract keywords with additional filtering
    keywords = [
        token.text for token in doc 
        if token.pos_ in include_pos
        and len(token.text) >= min_length
        and not token.is_stop
        and token.text.isalnum()
    ]
    
    # Remove duplicates while preserving order
    return list(dict.fromkeys(keywords))

## Test the function
'''keywords = extract_keywords("J_CV.docx")
print(keywords)'''

