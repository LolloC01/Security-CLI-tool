from dataclasses import dataclass
from .file_entry import FileEntry, FileEdited
from pathlib import Path


@dataclass
class Manifest:
    directory: Path
    algorithm: str
    directory_hash: str
    file_count: int
    files: list[FileEntry]

@dataclass
class ManifestComparison:
    new_files: list[FileEntry]
    removed_files: list[FileEntry]
    edited_files: list[FileEdited]