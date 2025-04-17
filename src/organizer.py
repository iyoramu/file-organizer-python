from pathlib import Path
from typing import List, Dict
from .utils.file_utils import (
    get_file_extension,
    create_directory,
    get_files_in_directory,
    move_file,
    get_standard_folder_name
)
from .utils.logger import FileOrganizerLogger

class FileOrganizer:
    def __init__(self, directory: str):
        self.directory = Path(directory).resolve()
        self.logger = FileOrganizerLogger()
        self._validate_directory()

    def _validate_directory(self) -> None:
        """Validate that directory exists and is accessible"""
        if not self.directory.exists():
            raise FileNotFoundError(f"Directory not found: {self.directory}")
        if not self.directory.is_dir():
            raise NotADirectoryError(f"Path is not a directory: {self.directory}")

    def organize_files(self, custom_mapping: Dict[str, str] = None) -> None:
        """Organize files in the directory"""
        self.logger.info(f"Organizing files in: {self.directory}")
        
        files = get_files_in_directory(str(self.directory))
        if not files:
            self.logger.info("No files found to organize")
            return

        for file_path in files:
            try:
                self._process_file(file_path, custom_mapping)
            except Exception as e:
                self.logger.error(f"Error processing file {file_path}: {str(e)}")

    def _process_file(self, file_path: str, custom_mapping: Dict[str, str] = None) -> None:
        """Process individual file"""
        extension = get_file_extension(file_path)
        if not extension:
            self.logger.warning(f"No extension found for file: {file_path}")
            return

        # Get folder name (check custom mapping first, then standard)
        folder_name = None
        if custom_mapping and extension in custom_mapping:
            folder_name = custom_mapping[extension]
        else:
            folder_name = get_standard_folder_name(extension)

        if not folder_name:
            self.logger.warning(f"No folder mapping for extension: {extension}")
            return

        # Create destination folder and move file
        dest_folder = self.directory / folder_name
        create_directory(str(dest_folder))
        
        dest_path = dest_folder / Path(file_path).name
        move_file(file_path, str(dest_path))
        
        self.logger.info(f"Moved {file_path} to {dest_path}")
