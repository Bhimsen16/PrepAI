import io
from pypdf import PdfReader

def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extracts raw text content page-by-page from an uploaded PDF byte stream."""
    pdf_file = io.BytesIO(file_bytes)
    reader = PdfReader(pdf_file)
    
    extracted_text = []
    for page_num, page in enumerate(reader.pages):
        page_text = page.extract_text()
        if page_text:
            extracted_text.append(f"--- Page {page_num + 1} ---\n{page_text.strip()}")
            
    return "\n\n".join(extracted_text)