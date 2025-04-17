import pytest
import os
import tempfile
from pathlib import Path
from src.utils.file_utils import (
    get_file_extension,
    create_directory,
    get_files_in_directory,
    move_file,
    get_standard_folder_name
)

def test_get_file_extension():
    assert get_file_extension("file.txt") == "txt"
    assert get_file_extension("image.JPG") == "jpg"
    assert get_file_extension("no_extension") == ""
    assert get_file_extension("path/to/file.pdf") == "pdf"

def test_create_directory(tmp_path):
    new_dir = tmp_path / "new_folder"
    create_directory(str(new_dir))
    assert new_dir.exists() and new_dir.is_dir()

def test_get_files_in_directory(tmp_path):
    # Create test files
    (tmp_path / "file1.txt").touch()
    (tmp_path / "file2.jpg").touch()
    (tmp_path / "subdir").mkdir()
    
    files = get_files_in_directory(str(tmp_path))
    assert len(files) == 2
    assert any("file1.txt" in f for f in files)
    assert any("file2.jpg" in f for f in files)

def test_move_file(tmp_path):
    src = tmp_path / "source.txt"
    dest = tmp_path / "destination.txt"
    src.touch()
    
    move_file(str(src), str(dest))
    assert not src.exists()
    assert dest.exists()

def test_get_standard_folder_name():
    assert get_standard_folder_name("jpg") == "Images"
    assert get_standard_folder_name("pdf") == "Documents"
    assert get_standard_folder_name("mp3") == "Audio"
    assert get_standard_folder_name("unknown") is None
