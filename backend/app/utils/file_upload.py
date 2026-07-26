import os
import shutil
import uuid
from pathlib import Path

from fastapi import HTTPException, UploadFile, status


class FileUpload:

    @staticmethod
    def save_file(
        file: UploadFile,
        folder: str,
        allowed_extensions: list[str],
    ) -> str:

        extension = Path(file.filename).suffix.lower()

        if extension not in allowed_extensions:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Only {', '.join(allowed_extensions)} files are allowed.",
            )

        filename = f"{uuid.uuid4()}{extension}"

        filepath = os.path.join(folder, filename)

        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return filepath.replace("\\", "/")