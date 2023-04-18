from fastapi import HTTPException, UploadFile


def validate_upload_file(file: UploadFile) -> None:
    filename = file.filename

    if filename is None:
        raise HTTPException(status_code=415, detail="No file provided")

    fileExtension = filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not fileExtension:
        raise HTTPException(status_code=415, detail="Unsupported file provided.")
