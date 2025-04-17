import click
import json
from pathlib import Path
from typing import Dict
from .organizer import FileOrganizer
from .utils.logger import FileOrganizerLogger

logger = FileOrganizerLogger()

@click.group()
@click.version_option("1.0.0")
def cli():
    """File Organizer CLI - Organize your files by type"""
    pass

@cli.command()
@click.argument("directory", type=click.Path(exists=True, file_okay=False))
@click.option("--mapping", help="Path to custom extension-folder mapping JSON file")
def organize(directory, mapping):
    """Organize files in the specified directory"""
    try:
        custom_mapping = None
        if mapping:
            with open(mapping, 'r') as f:
                custom_mapping = json.load(f)
            logger.info(f"Loaded custom mapping from: {mapping}")

        organizer = FileOrganizer(directory)
        organizer.organize_files(custom_mapping)
        logger.info("File organization completed successfully")
    except Exception as e:
        logger.error(f"Error organizing files: {str(e)}")
        raise click.ClickException(str(e))

@cli.command()
@click.argument("directory", type=click.Path(exists=True, file_okay=False))
def preview(directory):
    """Preview what files would be moved where (dry run)"""
    try:
        organizer = FileOrganizer(directory)
        files = get_files_in_directory(directory)
        
        if not files:
            click.echo("No files found to organize")
            return

        click.echo("File organization preview:")
        click.echo("=" * 50)
        
        for file_path in files:
            extension = get_file_extension(file_path)
            if not extension:
                click.echo(f"{file_path} -> (no extension, will be skipped)")
                continue
            
            folder_name = get_standard_folder_name(extension)
            if not folder_name:
                click.echo(f"{file_path} -> (no folder mapping for .{extension})")
                continue
            
            click.echo(f"{file_path} -> {folder_name}/")

        click.echo("=" * 50)
        click.echo(f"Total files: {len(files)}")
    except Exception as e:
        logger.error(f"Error during preview: {str(e)}")
        raise click.ClickException(str(e))

if __name__ == "__main__":
    cli()
