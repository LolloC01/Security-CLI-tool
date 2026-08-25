from dataclasses import dataclass
from .file_entry import FileEntry, FileEdited


@dataclass
class Manifest:
    directory: str
    algorithm: str
    directory_hash: str
    file_count: int
    files: list[FileEntry]

@dataclass
class ManifestComparison:
    new_files: list[FileEntry]
    removed_files: list[FileEntry]
    edited_files: list[FileEdited]