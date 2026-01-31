import uuid


def file_namer(original_filename: str, content_type: str) -> str:
    """Genera un nombre único para el archivo subido."""
    ext = "jpg"
    if content_type and "/" in content_type:
        ext = content_type.split("/")[1].lower()
        if ext == "jpeg":
            ext = "jpg"
    return f"{uuid.uuid4()}.{ext}"
