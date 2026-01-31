VALID_EXTENSIONS = {"jpg", "jpeg", "png", "gif"}


def file_filter(content_type: str) -> bool:
    """Indica si el tipo MIME corresponde a una imagen permitida."""
    if not content_type or "/" not in content_type:
        return False
    ext = content_type.split("/")[1].lower()
    if ext == "jpeg":
        ext = "jpg"
    return ext in VALID_EXTENSIONS
