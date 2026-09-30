from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.pdf_service import extract_text_from_pdf

router = APIRouter()

@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    # Validate file type
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    # Read file contents into memory
    contents = await file.read()
    
    # Extract text using service function
    extracted_text = extract_text_from_pdf(contents)
    
    if not extracted_text.strip():
        raise HTTPException(status_code=400, detail="Could not extract text from PDF. File might be empty or image-based.")
    
    return {
        "filename": file.filename,
        "character_count": len(extracted_text),
        "preview": extracted_text[:500] + "...",  # First 500 characters
        "full_text": extracted_text
    }