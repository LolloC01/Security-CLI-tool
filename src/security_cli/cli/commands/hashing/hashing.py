import hashlib
import os
from pathlib import Path
import blake3
from .algorithm import Algorithm
from .manifest import Manifest, ManifestComparison
from .file_entry import FileEntry, FileEdited

class HashFunctions:

    @staticmethod
    def file_hash(file_path: Path, algorithm: Algorithm) -> str:
        """
        Calculate the hash of a file using the specified algorithm.

        Args:
            file_path (Path): The path to the file.
            algorithm (Algorithm): The hashing algorithm to use.

        Returns:
            str: The calculated hash in hexadecimal format.
        """

        if algorithm == Algorithm.blake3:
            hash_func = blake3.blake3()
        else:
            hash_func = hashlib.new(algorithm.value)

        with open(file_path, "rb") as f:
            while chunk := f.read(1024 * 1024):  # Read in 1MB chunks
                hash_func.update(chunk)

        return hash_func.hexdigest()

    @staticmethod
    def text_hash(text: str, algorithm: Algorithm) -> str:
        """
        Calculate the hash of a text string using the specified algorithm.

        Args:
            text (str): The input text to hash.
            algorithm (Algorithm): The hashing algorithm to use.

        Returns:
            str: The calculated hash in hexadecimal format.
        """

        if algorithm == Algorithm.blake3:
            hash_func = blake3.blake3()
        else:
            hash_func = hashlib.new(algorithm.value)

        hash_func.update(text.encode("utf-8"))

        return hash_func.hexdigest()

    @staticmethod
    def compare_hashes(hash1: str, hash2: str) -> bool:
        """
        Compare two hash values.

        Args:
            hash1 (str): The first hash value.
            hash2 (str): The second hash value.

        Returns:
            bool: True if the hashes are equal, False otherwise.
        """
        return hash1 == hash2

    @staticmethod
    def create_manifest(directory_path: Path, algorithm: Algorithm) -> Manifest:
        """
        Calculate the hash of a directory by hashing the contents of all files within it.

        Args:
            directory_path (Path): The path to the directory.
            algorithm (Algorithm): The hashing algorithm to use.

        Returns:
            Manifest: A manifest containing the directory hash and file information.
        """
        directory = Path(directory_path)
        manifest: Manifest = Manifest(directory=directory_path, algorithm=algorithm.value, directory_hash="", file_count=0, files=[])

        files = sorted(
            [
                file
                for file in directory.rglob("*")
                if file.is_file()
            ]
        )

        for file_path in files:
            manifest.file_count += 1

            relative_path = file_path.relative_to(directory)

            digest = HashFunctions.file_hash(file_path, algorithm)

            file: FileEntry = FileEntry(
                path=str(relative_path),
                size=os.path.getsize(file_path),
                digest=digest
            )

            manifest.files.append(file)

        manifest.directory_hash = HashFunctions.manifest_hash(manifest, algorithm)

        return manifest

    @staticmethod
    def manifest_hash(manifest: Manifest, algorithm: Algorithm) -> str:
        """
        Calculate the hash of a manifest.

        Args:
            manifest (Manifest): The manifest object.
            algorithm (Algorithm): The hashing algorithm to use.

        Returns:
            str: The calculated hash in hexadecimal format.
        """
        hash: str = HashFunctions.text_hash(
            "".join(
                f"{file.path}:{file.digest}"
                for file in sorted(manifest.files, key=lambda x: x.path)
            ),
            algorithm
        )

        return hash

    @staticmethod
    def compare_manifests(manifest1: Manifest, manifest2: Manifest) -> bool:
        """
        Compare two manifests.

        Args:
            manifest1 (Manifest): The first manifest.
            manifest2 (Manifest): The second manifest.

        Returns:
            bool: True if the manifests are equal, False otherwise.
        """
        return manifest1.directory_hash == manifest2.directory_hash

    @staticmethod
    def compare_directories(manifest1: Manifest, manifest2: Manifest) -> ManifestComparison:
        """
        Compare two directories by comparing their manifests.

        Args:
            manifest1 (Manifest): The first manifest.
            manifest2 (Manifest): The second manifest.

        Returns:
            ManifestComparison: A comparison of the two manifests, including new, removed, and edited files.
        """
        edited_files = [
            FileEdited(old_file=file1, new_file=file2)
            for file1 in manifest1.files
            for file2 in manifest2.files
            if file1.path == file2.path and file1.digest != file2.digest
        ]
        new_files = [file for file in manifest2.files if file not in manifest1.files and file not in [edited.new_file for edited in edited_files]]
        removed_files = [file for file in manifest1.files if file not in manifest2.files and file not in [edited.old_file for edited in edited_files]]

        return ManifestComparison(
            new_files=new_files,
            removed_files=removed_files,
            edited_files=edited_files
        )