from pathlib import Path

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def display_file_hash(file_path: Path, algorithm: str, file_hash: str):
    """
    Display the hash information in a formatted table.

    Args:
        file_path (Path): The path to the file.
        algorithm (str): The hashing algorithm used.
        file_hash (str): The calculated hash value.
    """
    table = Table(title="File Hash")

    table.add_column("Property", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("File", str(file_path))
    table.add_row("Size", f"{Path(file_path).stat().st_size} bytes")
    table.add_row("Algorithm", algorithm)
    table.add_row("Hash", file_hash)

    console.print(table)

def display_text_hash(text: str, algorithm: str, text_hash: str):
    """
    Display the hash of a text string.

    Args:
        text (str): The input text.
        algorithm (str): The hashing algorithm used.
        text_hash (str): The calculated hash value.
    """
    console.print(f"Text: {text}")
    console.print(f"Algorithm: {algorithm}")
    console.print(f"Hash: {text_hash}")

def display_successful_verification(file_path: str, algorithm: str, hash_value: str):
    """
    Display the result of a successful hash verification.

    Args:
        file_path (str): The path to the verified file.
        algorithm (str): The hashing algorithm used.
        hash_value (str): The calculated hash value of the file.
    """
    console.print(
        Panel.fit(
            f"[bold green]✓ Verification successful[/bold green]\n\n"
            f"[cyan]File:[/cyan] {file_path}\n"
            f"[cyan]Algorithm:[/cyan] {algorithm}\n"
            f"[cyan]Hash:[/cyan] {hash_value}",
            title="Hash Verification",
            border_style="green",
        )
    )

def display_failed_verification(file_path: str, algorithm: str, known_hash: str, calculated_hash: str):
    """
    Display the result of a failed hash verification.

    Args:
        file_path (str): The path to the file being verified.
        algorithm (str): The hashing algorithm used.
        known_hash (str): The known hash value to compare against.
        calculated_hash (str): The calculated hash value of the file.
    """
    console.print(
        Panel.fit(
            f"[bold red]✗ Verification failed[/bold red]\n\n"
            f"[cyan]File:[/cyan] {file_path}\n"
            f"[cyan]Algorithm:[/cyan] {algorithm}\n"
            f"[cyan]Known Hash:[/cyan] {known_hash}\n"
            f"[cyan]Calculated Hash:[/cyan] {calculated_hash}",
            title="Hash Verification",
            border_style="red",
        )
    )

def display_success_comparison(file1: str, file2: str, algorithm: str, hash_value: str):
    """
    Display the result of a successful hash comparison between two files.

    Args:
        file1 (str): The path to the first file.
        file2 (str): The path to the second file.
        algorithm (str): The hashing algorithm used.
        hash_value (str): The common hash value of both files.
    """
    console.print(
        Panel.fit(
            f"[bold green]✓ Integrity check passed[/bold green]\n\n"
            f"[cyan]Algorithm:[/cyan] {algorithm}\n\n"
            f"[cyan]Files:[/cyan]\n"
            f"  • {file1}\n"
            f"  • {file2}\n\n"
            f"[cyan]Digest:[/cyan]\n"
            f"  {hash_value}",
            title="Hash Verification",
            border_style="green",
        )
    )

def display_failure_comparison(file1: str, file2: str, algorithm: str):
    """
    Display the result of a failed hash comparison between two files.

    Args:
        file1 (str): The path to the first file.
        file2 (str): The path to the second file.
        algorithm (str): The hashing algorithm used.
    """
    console.print(
        Panel.fit(
            f"[bold red]✗ Integrity check failed[/bold red]\n\n"
            f"[cyan]Algorithm:[/cyan] {algorithm}\n\n"
            f"[cyan]Files:[/cyan]\n"
            f"  • {file1}\n"
            f"  • {file2}",
            title="Hash Verification",
            border_style="red",
        )
    )

def display_algorithm():
    """
    Display the name of a hashing algorithm.

    Args:
        algorithm (str): The name of the hashing algorithm.
    """
    table = Table(
        title="Supported Hash Algorithms",
        title_style="bold cyan",
        border_style="blue",
        header_style="bold white",
    )

    table.add_column("Algorithm", style="cyan", justify="center")
    table.add_column("Type", style="magenta")
    table.add_column("Digest Size", justify="center")
    table.add_column("Security Status", justify="center")
    table.add_column("Recommended Usage", style="green")

    algorithms = [
        (
            "MD5",
            "Legacy",
            "128 bit",
            "[bold red]NOT SECURE[/bold red]",
            "Checksums only, no security use",
        ),
        (
            "SHA-1",
            "SHA-2 predecessor",
            "160 bit",
            "[bold red]DEPRECATED[/bold red]",
            "Compatibility with old systems",
        ),
        (
            "SHA-256",
            "SHA-2",
            "256 bit",
            "[bold green]SECURE[/bold green]",
            "General purpose integrity verification",
        ),
        (
            "SHA-512",
            "SHA-2",
            "512 bit",
            "[bold green]SECURE[/bold green]",
            "High security applications",
        ),
        (
            "BLAKE2b",
            "BLAKE family",
            "Up to 512 bit",
            "[bold green]SECURE[/bold green]",
            "Fast cryptographic hashing",
        ),
        (
            "BLAKE3",
            "BLAKE family",
            "256 bit",
            "[bold green]SECURE[/bold green]",
            "High performance hashing",
        ),
    ]

    for algorithm in algorithms:
        table.add_row(*algorithm)

    console.print(
        Panel.fit(
            table,
            title="Hash Algorithms Reference",
            border_style="cyan",
        )
    )

def display_directory_hash(directory_path: str, algorithm: str, directory_hash: str, file_count: int):
    """
    Display the hash of a directory and the number of files hashed.

    Args:
        directory_path (str): The path to the directory.
        algorithm (str): The hashing algorithm used.
        directory_hash (str): The calculated hash value of the directory.
        file_count (int): The number of files hashed in the directory.
    """
    console.print(
        Panel.fit(
            f"[bold green]Directory Hash Calculation[/bold green]\n\n"
            f"[cyan]Directory:[/cyan] {directory_path}\n"
            f"[cyan]Algorithm:[/cyan] {algorithm}\n"
            f"[cyan]Hash:[/cyan] {directory_hash}\n"
            f"[cyan]Files Hashed:[/cyan] {file_count}",
            title="Directory Hash Result",
            border_style="green",
        )
    )

def display_manifest(manifest_path: str, algorithm: str, directory_hash: str, file_count: int):
    """
    Display the contents of a manifest file.

    Args:
        manifest_path (str): The path to the manifest file.
        algorithm (str): The hashing algorithm used.
        directory_hash (str): The calculated hash value of the directory.
        file_count (int): The number of files hashed in the directory.
    """
    console.print(
        Panel.fit(
            f"[bold green]Manifest File[/bold green]\n\n"
            f"[cyan]Manifest Path:[/cyan] {manifest_path}\n"
            f"[cyan]Algorithm:[/cyan] {algorithm.value}\n"
            f"[cyan]Directory Hash:[/cyan] {directory_hash}\n"
            f"[cyan]Files Hashed:[/cyan] {file_count}",
            title="Manifest Result",
            border_style="green",
        )
    )

def display_successful_dir_comparison(directory1: str, directory2: str, algorithm: str, directory_hash: str):
    """
    Display the result of a successful directory comparison.

    Args:
        directory1 (str): The path to the first directory.
        directory2 (str): The path to the second directory.
        algorithm (str): The hashing algorithm used.
        directory_hash (str): The calculated hash value of the directories.
    """
    console.print(
        Panel.fit(
            f"[bold green]✓ Directory Comparison Successful[/bold green]\n\n"
            f"[cyan]Algorithm:[/cyan] {algorithm}\n\n"
            f"[cyan]Directory 1:[/cyan] {directory1}\n"
            f"[cyan]Directory 2:[/cyan] {directory2}\n\n"
            f"[cyan]Directory Hash:[/cyan] {directory_hash}",
            title="Directory Comparison Result",
            border_style="green",
        )
    )

def display_failed_dir_comparison(directory1: str, directory2: str, algorithm: str, comparison, verbose: bool = False):
    """
    Display the result of a failed directory comparison.

    Args:
        directory1 (str): The path to the first directory.
        directory2 (str): The path to the second directory.
        algorithm (str): The hashing algorithm used.
        comparison (ManifestComparison): The comparison result containing new, removed, and edited files.
        verbose (bool): Whether to display detailed information about the differences.
    """
    console.print(
        Panel.fit(
            f"[bold red]✗ Directory Comparison Failed[/bold red]\n\n"
            f"[cyan]Algorithm:[/cyan] {algorithm}\n\n"
            f"[cyan]Directory 1:[/cyan] {directory1}\n"
            f"[cyan]Directory 2:[/cyan] {directory2}\n\n"
            f"[green]Added:[/green] {len(comparison.new_files)}\n"
            f"[red]Removed:[/red] {len(comparison.removed_files)}\n"
            f"[yellow]Modified:[/yellow] {len(comparison.edited_files)}",
            title="Integrity Check Result",
            border_style="red",
        )
    )

    if not verbose:
        return


    # -----------------------
    # Added files
    # -----------------------

    if comparison.new_files:

        table = Table(
            title=f"Added Files ({len(comparison.new_files)})",
            border_style="green"
        )

        table.add_column(
            "File",
            style="cyan"
        )

        table.add_column(
            "Size",
            justify="right",
            style="green"
        )

        table.add_column(
            "Hash",
            style="yellow"
        )

        for file in comparison.new_files:
            table.add_row(
                file.path,
                f"{file.size} bytes",
                shorten_hash(file.digest)
            )

        console.print(table)


    # -----------------------
    # Removed files
    # -----------------------

    if comparison.removed_files:

        table = Table(
            title=f"Removed Files ({len(comparison.removed_files)})",
            border_style="red"
        )

        table.add_column(
            "File",
            style="cyan"
        )

        table.add_column(
            "Size",
            justify="right",
            style="red"
        )

        table.add_column(
            "Hash",
            style="yellow"
        )

        for file in comparison.removed_files:
            table.add_row(
                file.path,
                f"{file.size} bytes",
                shorten_hash(file.digest)
            )

        console.print(table)


    # -----------------------
    # Modified files
    # -----------------------

    if comparison.edited_files:

        console.print(
            f"\n[bold yellow]Modified Files ({len(comparison.edited_files)})[/bold yellow]"
        )

        for edited_file in comparison.edited_files:

            console.print(
                Panel(
                    f"""
[cyan]File:[/cyan] {edited_file.old_file.path}

[red]OLD[/red]
  Size: {edited_file.old_file.size} bytes
  Hash: {shorten_hash(edited_file.old_file.digest)}

[green]NEW[/green]
  Size: {edited_file.new_file.size} bytes
  Hash: {shorten_hash(edited_file.new_file.digest)}
                    """,
                    border_style="yellow"
                )
            )

def shorten_hash(hash_value: str, length: int = 16) -> str:
    if len(hash_value) <= length:
        return hash_value

    return f"{hash_value[:length]}..."




