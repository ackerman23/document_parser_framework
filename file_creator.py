import os

# Define the project structure
project_structure = {
    "document_parser": {
        "input_processing": [
            "pdf_handler.py",
            "word_handler.py"
        ],
        "nlp": [
            "summarizer.py",
            "keyword_extractor.py"
        ],
        "pipelines": [
            "document_pipeline.py"
        ],
        "tests": [
            "test_pdf_parsing.py",
            "test_word_parsing.py"
        ],
        "utils": [
            "file_utils.py"
        ],
    }
}

# Create the project structure
def create_project_structure(base_path, structure):
    for folder, files in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            create_file(folder_path, file)

# Function to create the file and write boilerplate content
def create_file(folder_path, filename):
    file_path = os.path.join(folder_path, filename)
    
    if "handler" in filename:
        content = '''import os

# Example handler code for handling {file_type} documents
# This file contains basic code for extracting text from {file_type} documents.

def extract_text_from_{file_type}(file_path):
    pass
    '''
        file_type = filename.split('_')[0]
    with open(file_path, "w") as f:
        f.write(content.format(file_type=file_type))
        
    print(f"Created {file_path}")

def create_tests(folder_path, filename):
    content = '''import unittest
from input_processing.{file_type}_handler import extract_text_from_{file_type}

class Test{file_type.capitalize()}Parser(unittest.TestCase):
    def test_extract_text(self):
        text = extract_text_from_{file_type}('sample_document.{file_type}')
        self.assertGreater(len(text), 0)
        
if __name__ == '__main__':
    unittest.main()
'''
    file_type = filename.split('_')[0]
    with open(file_path, "w") as f:
        f.write(content.format(file_type=file_type.capitalize()))
    print(f"Created {file_path}")


def main():
    # Base path where the project will be created
    base_path = os.getcwd()
    
    # Create the project structure and files
    create_project_structure(base_path, project_structure)


# Run the script to create files
main()

