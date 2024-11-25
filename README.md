# Document Parser Framework

A powerful Python framework for parsing, summarizing, and extracting information from documents. This framework combines NLP capabilities to provide document summaries, keyword extraction, and structured information extraction.

# Future Work

- [ ] Add support for more file types (e.g., DOCX, TXT)
- [ ] Implement more advanced NLP techniques for better summarization and keyword extraction
- [ ] Add error handling and logging for better debugging and monitoring
- [ ] Add support for more advanced NLP techniques for better summarization and keyword extraction

## Features

- 📄 PDF and Text file processing
- 📝 Text summarization using BART
- 🔑 Keyword extraction using SpaCy
- 📊 Table extraction from documents
- 🔄 Modular pipeline architecture

## Prerequisites

- Python 3.10+
- Conda or Miniconda (recommended for environment management)

## Installation

1. Clone the repository:
bash
git clone [your-repository-url]
cd document_parser_framework

2. Create and activate a conda environment:

bash
conda create -n document-parser-env python=3.10
conda activate document-parser-env

3. Install required packages:
bash
pip install -r requirements.txt
bash
python -m spacy download en_core_web_sm

## Project Structure

document_parser_framework/
├── pipelines/
│   └── document_pipeline.py
├── nlp/
│   ├── keyword_extractor.py
│   ├── summarizer.py
│   └── table_extractor.py
├── utils/
│   └── text_utils.py
├── requirements.txt
└── README.md

## Usage

### Basic Usage

```python
from pipelines.document_pipeline import process_pdf

# Process a PDF document
result = process_pdf("path/to/your/document.pdf")

# Access the results
text = result['text']           # Original text
summary = result['summary']     # Generated summary
keywords = result['keywords']   # Extracted keywords
tables = result['tables']       # Extracted tables
```

### Advanced Usage

```python
from nlp.summarizer import summarize_text
from nlp.keyword_extractor import extract_keywords
from nlp.table_extractor import extract_tables

# Individual component usage
summary = summarize_text(text)
keywords = extract_keywords(text)
tables = extract_tables(text)
```

## Configuration

The framework can be configured through various parameters:

### Summarization
- `chunk_size`: Maximum size of text chunks for processing (default: 1024)
- `min_length_ratio`: Minimum summary length ratio (default: 0.3)
- `max_length_ratio`: Maximum summary length ratio (default: 0.7)

### Keyword Extraction
- `pos_tags`: Parts of speech to consider for keywords
- `min_freq`: Minimum frequency for keyword consideration

## Requirements

Main dependencies:
- transformers
- torch
- spacy
- pandas
- PyPDF2
- nltk

See `requirements.txt` for complete list.

## Common Issues and Solutions

1. SpaCy Model Error:
```bash
OSError: [E050] Can't find model 'en_core_web_sm'
```
Solution: Run `python -m spacy download en_core_web_sm`

2. Memory Issues:
If you encounter memory issues with large documents, try:
- Reducing chunk_size in summarizer
- Processing documents in smaller sections

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Acknowledgments

- BART model from Hugging Face
- SpaCy for NLP processing
- PyPDF2 for PDF handling

## Contact

Jihad Garti - [jihad.garti2@gmail.com]



