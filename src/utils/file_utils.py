import os
import shutil
from pathlib import Path
from typing import Dict, List, Optional

def get_file_extension(file_path: str) -> str:
    """Get the lowercase file extension without the dot"""
    return Path(file_path).suffix[1:].lower()

def create_directory(dir_path: str) -> None:
    """Create directory if it doesn't exist"""
    Path(dir_path).mkdir(parents=True, exist_ok=True)

def get_files_in_directory(directory: str) -> List[str]:
    """Get all files in directory (non-recursive)"""
    return [
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f))
    ]

def move_file(src: str, dest: str) -> None:
    """Move file from src to dest"""
    shutil.move(src, dest)

def get_standard_folder_name(extension: str) -> Optional[str]:
    """Get standard folder name for file extension"""
    extension = extension.lower()
    folder_map = {
        # Images
        'jpg': 'Images',
        'jpeg': 'Images',
        'png': 'Images',
        'gif': 'Images',
        'webp': 'Images',
        'svg': 'Images',
        'bmp': 'Images',
        'tiff': 'Images',
        # Documents
        'pdf': 'Documents',
        'doc': 'Documents',
        'docx': 'Documents',
        'xls': 'Documents',
        'xlsx': 'Documents',
        'ppt': 'Documents',
        'pptx': 'Documents',
        'txt': 'Documents',
        'md': 'Documents',
        'csv': 'Documents',
        # Archives
        'zip': 'Archives',
        'rar': 'Archives',
        'tar': 'Archives',
        'gz': 'Archives',
        '7z': 'Archives',
        # Audio
        'mp3': 'Audio',
        'wav': 'Audio',
        'ogg': 'Audio',
        'flac': 'Audio',
        'aac': 'Audio',
        # Video
        'mp4': 'Videos',
        'mov': 'Videos',
        'avi': 'Videos',
        'mkv': 'Videos',
        'wmv': 'Videos',
        'flv': 'Videos',
        # Code
        'py': 'Code',
        'js': 'Code',
        'html': 'Code',
        'css': 'Code',
        'json': 'Code',
        'xml': 'Code',
        'java': 'Code',
        'cpp': 'Code',
        'c': 'Code',
        'h': 'Code',
        'sh': 'Code',
    }
    return folder_map.get(extension, None)
