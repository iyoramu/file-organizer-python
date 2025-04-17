# File Organizer CLI (file-organizer-python)

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)

A professional command-line tool to automatically organize files in any directory by their types (extensions). Perfect for keeping your Downloads, Documents, or any messy folder clean and organized.

## Features

- 📂 **Automatic File Organization**: Sorts files into logical folders (Images, Documents, Videos, etc.)
- 🛠 **Customizable Mappings**: Define your own extension-to-folder rules via JSON
- 👀 **Dry Run Mode**: Preview changes before executing
- 📝 **Detailed Logging**: Full audit trail of all operations
- 🚦 **Error Handling**: Robust validation and error recovery
- 🖥 **Cross-Platform**: Works on Windows, macOS, and Linux
- ⚡ **Fast Execution**: Processes thousands of files in seconds

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Install from source
```bash
git clone https://github.com/iyoramu/file-organizer-python.git
cd file-organizer-python
pip install -e .
```

### Install via pip (when published)
```bash
pip install file-organizer-cli
```

## Usage

### Basic Organization
```bash
file-organizer organize ~/Downloads
```

### Custom Folder Mapping
Create a JSON file (e.g., `custom_mapping.json`):
```json
{
    "epub": "Ebooks",
    "psd": "Design_Files",
    "ai": "Design_Files",
    "indd": "Design_Files"
}
```
Then run:
```bash
file-organizer organize ~/Documents --mapping custom_mapping.json
```

### Preview Mode (Dry Run)
```bash
file-organizer preview ~/Desktop
```

## Default Folder Structure

The tool automatically organizes files into these standard folders:

| Category      | Extensions                                |
|---------------|------------------------------------------|
| Images        | .jpg, .jpeg, .png, .gif, .webp, .svg    |
| Documents     | .pdf, .doc, .docx, .xls, .xlsx, .txt    |
| Archives      | .zip, .rar, .tar, .gz, .7z              |
| Audio         | .mp3, .wav, .ogg, .flac, .aac           |
| Videos        | .mp4, .mov, .avi, .mkv, .wmv            |
| Code          | .py, .js, .html, .css, .json, .java      |

## Advanced Configuration

### Customizing via JSON
Create a configuration file to:
- Override default folder names
- Add new file type mappings
- Group multiple extensions under custom categories

Example `config.json`:
```json
{
    "folder_names": {
        "Images": "Pictures",
        "Documents": "Office_Docs"
    },
    "mappings": {
        "epub": "Ebooks",
        "md": "Markdown_Files"
    }
}
```

### Logging Configuration
Logs are output to console by default. To configure file logging:

1. Create `.env` file:
```ini
LOG_LEVEL=DEBUG
LOG_FILE=organizer.log
```
2. Run with environment variables:
```bash
file-organizer organize ~/Downloads
```

## Development

### Running Tests
```bash
python -m pytest tests/
```

### Building for Distribution
```bash
python setup.py sdist bdist_wheel
```

### Contributing
Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support
For issues or feature requests, please [open an issue](https://github.com/iyoramu/file-organizer-python/issues).

---

**Pro Tip**: Add an alias to your shell configuration for quick access:
```bash
alias fo='file-organizer organize'
```
Then simply run:
```bash
fo ~/Downloads
```
