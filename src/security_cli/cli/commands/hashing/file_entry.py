from dataclasses import dataclass


@dataclass
class FileEntry:
    path: str
    size: int
    digest: str

@dataclass
class FileEdited:
    old_file: FileEntry
    new_file: FileEntry