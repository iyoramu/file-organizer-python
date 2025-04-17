import pytest
import os
from pathlib import Path
from src.organizer import FileOrganizer
from src.utils.file_utils import get_files_in_directory

def test_organizer_initialization(tmp_path):
    organizer = FileOrganizer(str(tmp_path))
    assert organizer.directory == tmp_path.resolve()

def test_organize_files(tmp_path):
    # Create test files
    (tmp_path / "test.jpg").touch()
    (tmp_path / "document.pdf").touch()
    (tmp_path / "unknown.xyz").touch()
    
    organizer = FileOrganizer(str(tmp_path))
    organizer.organize_files()
    
    # Check files were moved
    assert (tmp_path / "Images/test.jpg").exists()
    assert (tmp_path / "Documents/document.pdf").exists()
    assert (tmp_path / "unknown.xyz").exists()  # Should remain unmoved
    
    # Check original files are gone
    assert not (tmp_path / "test.jpg").exists()
    assert not (tmp_path / "document.pdf").exists()

def test_custom_mapping(tmp_path):
    # Create test file and custom mapping
    (tmp_path / "custom.ext").touch()
    custom_mapping = {"ext": "CustomFiles"}
    
    organizer = FileOrganizer(str(tmp_path))
    organizer.organize_files(custom_mapping)
    
    assert (tmp_path / "CustomFiles/custom.ext").exists()
    assert not (tmp_path / "custom.ext").exists()

def test_invalid_directory():
    with pytest.raises(FileNotFoundError):
        FileOrganizer("/nonexistent/path")
    
    with tempfile.NamedTemporaryFile() as tmp_file:
        with pytest.raises(NotADirectoryError):
            FileOrganizer(tmp_file.name)
