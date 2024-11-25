from setuptools import setup, find_packages

setup(
    name="document_parser",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "python-docx",
        "pdfplumber",
        "spaCy",
        "transformers",
    ]
)
