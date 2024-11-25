from transformers import pipeline
from docx import Document
import torch
def read_docx(file_path):
    try:
        doc = Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            if para.text.strip():  # Only include non-empty paragraphs
                full_text.append(para.text)
        text = ' '.join(full_text)
        if not text:
            raise ValueError("Document appears to be empty")
        return text
    except Exception as e:
        raise Exception(f"Error reading document {file_path}: {str(e)}")

def calculate_summary_length(text_length, is_chunk=False):
    """Calculate appropriate summary lengths based on text size."""
    # Estimate token count (rough approximation: 4 characters per token)
    estimated_tokens = text_length // 4
    
    # For chunks, use more conservative lengths
    if is_chunk:
        ratio = 0.4  # 40% of input length for chunks
    else:
        ratio = 0.5  # 50% of input length for final summary
    
    # Calculate target lengths
    max_length = int(estimated_tokens * ratio)
    min_length = int(max_length * 0.4)  # Min length is 40% of max length
    
    # Apply reasonable limits
    max_length = min(max_length, 500)  # Cap at 500 tokens
    max_length = max(max_length, 100)   # At least 100 tokens
    min_length = min(min_length, max_length - 50)  # Ensure gap with max_length
    min_length = max(min_length, 30)    # At least 30 tokens
    
    return min_length, max_length

def chunk_text(text, max_chunk_size=3000):
    """Split text into chunks of approximately max_chunk_size characters."""
    words = text.split()
    chunks = []
    current_chunk = []
    current_size = 0
    
    for word in words:
        word_len = len(word) + 1  # +1 for the space
        if current_size + word_len > max_chunk_size and current_chunk:
            chunks.append(' '.join(current_chunk))
            current_chunk = []
            current_size = 0
        current_chunk.append(word)
        current_size += word_len
    
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    print(f"Split into {len(chunks)} chunks")  # Debug info
    return chunks

def summarize_text(text):
    if not isinstance(text, str) or len(text.strip()) < 30:
        raise ValueError("Input text must be a string with at least 30 characters")
    
    # Calculate appropriate summary lengths
    text_length = len(text)
    
    summarizer = pipeline(
        "summarization",
        model="facebook/bart-large-cnn",
        device="cpu"
    )
    
    # Split into chunks if text is too long
    chunks = chunk_text(text)
    chunk_summaries = []
    
    # Summarize each chunk
    print("Summarizing chunks...")  # Debug info
    for i, chunk in enumerate(chunks, 1):
        try:
            chunk_min_length, chunk_max_length = calculate_summary_length(len(chunk), is_chunk=True)
            print(f"Processing chunk {i}/{len(chunks)} - Target length: {chunk_min_length}-{chunk_max_length}")
            
            summary = summarizer(
                chunk,
                max_length=chunk_max_length,
                min_length=chunk_min_length,
                length_penalty=2.0,
                num_beams=4,
                do_sample=False
            )
            chunk_summaries.append(summary[0]['summary_text'])
        except Exception as e:
            print(f"Warning: Error summarizing chunk {i}: {str(e)}")
            continue
    
    # If we have multiple summaries, create a final summary of summaries
    if len(chunk_summaries) > 1:
        print("\n=== Chunk Summaries ===")
        for i, chunk_sum in enumerate(chunk_summaries, 1):
            print(f"\nChunk {i}:\n{chunk_sum}")
            
        print("\n=== Creating Final Summary ===")
        combined_summary = " ".join(chunk_summaries)
        try:
            final_min_length, final_max_length = calculate_summary_length(len(combined_summary))
            print(f"Final summary target length: {final_min_length}-{final_max_length}")
            
            final_summary = summarizer(
                combined_summary,
                max_length=final_max_length,
                min_length=final_min_length,
                length_penalty=2.0,
                num_beams=4,
                do_sample=False
            )
            print("\n=== Final Summary ===")
            return final_summary[0]['summary_text']
        except Exception as e:
            print(f"Warning: Error in final summarization: {str(e)}")
            return "Individual chunk summaries:\n\n" + "\n\n".join(chunk_summaries)
    elif len(chunk_summaries) == 1:
        return chunk_summaries[0]
    else:
        raise ValueError("No successful summaries were generated")

# Test the function
try:
    docx_text = read_docx("/Users/jihadgarti/Desktop/research/adaptive learning research/Adaptive Learning Technology.docx")
    print("Document content length:", len(docx_text))
    summary = summarize_text(docx_text)
    print("Summary:", summary)
except Exception as e:
    print(f"Error: {e}")
