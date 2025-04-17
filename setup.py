from setuptools import setup, find_packages

setup(
    name="file-organizer",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "click>=8.1.3",
        "python-dotenv>=0.21.0"
    ],
    entry_points={
        "console_scripts": [
            "file-organizer=file_organizer.main:cli",
        ],
    },
    python_requires=">=3.8",
)
