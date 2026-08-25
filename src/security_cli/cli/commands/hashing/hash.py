'''
appsec hash
├── hash-file       Calcola l'hash di un file  TODO: più di un file
├── hash-text       Calcola l'hash di una stringa
├── verify          Verifica un file contro un hash noto
├── compare         Confronta gli hash di due file
├── manifest        Crea manifest una cartella [path, algoritmo, hash, numero file, {file: hash}]
├── dir-compare     Calcola le differenze tra i manifest di due cartelle
└── algorithms      Mostra gli algoritmi disponibili
'''

from pathlib import Path
import typer

from manifest import Manifest, ManifestComparison
import output as output_utils
from algorithm import Algorithm
import hashing as hashing_utils

app = typer.Typer()

@app.command()
def hash_file(
    file_path: Path = typer.Argument(..., exists=True, file_okay=True, dir_okay=False, readable=True),
    algorithm: Algorithm = typer.Option(Algorithm.blake2b, "--algorithm", "-a", prompt=True),
):
    file_hash = hashing_utils.file_hash(file_path, algorithm)

    output_utils.display_file_hash(file_path, algorithm.value, file_hash)

@app.command()
def hash_text(
    text: str = typer.Option(..., "--text", "-t", prompt=True),
    algorithm: Algorithm = typer.Option(Algorithm.blake2b, "--algorithm", "-a", prompt=True),
):
    text_hash = hashing_utils.text_hash(text, algorithm)
    output_utils.display_text_hash(text, algorithm.value, text_hash)

@app.command()
def verify(
    file_path: Path = typer.Argument(..., exists=True, file_okay=True, dir_okay=False, readable=True),
    algorithm: Algorithm = typer.Option(Algorithm.blake2b, "--algorithm", "-a", prompt=True),
    known_hash: str = typer.Option(..., "--hash", "-H", prompt=True)
):
    '''
    Verifica un file contro un hash noto
    '''
    calculated_hash = hashing_utils.file_hash(file_path, algorithm)

    if hashing_utils.compare_hashes(calculated_hash, known_hash):
        output_utils.display_successful_verification(file_path, algorithm.value, known_hash)
    else:
        output_utils.display_failed_verification(file_path, algorithm.value, known_hash, calculated_hash)

@app.command()
def compare(
    file1: Path = typer.Argument(..., exists=True, file_okay=True, dir_okay=False, readable=True),
    file2: Path = typer.Argument(..., exists=True, file_okay=True, dir_okay=False, readable=True),
    algorithm: Algorithm = typer.Option(Algorithm.blake2b, "--algorithm", "-a", prompt=True)
):

    hash1 = hashing_utils.file_hash(file1, algorithm)
    hash2 = hashing_utils.file_hash(file2, algorithm)

    if hashing_utils.compare_hashes(hash1, hash2):
        output_utils.display_success_comparison(file1, file2, algorithm.value, hash1)

    else:
        output_utils.display_failure_comparison(file1, file2, algorithm.value)

@app.command()
def manifest(
    directory_path: Path = typer.Argument(..., exists=True, file_okay=False, dir_okay=True),
    algorithm: Algorithm = typer.Option(Algorithm.blake2b, "--algorithm", "-a", prompt=True)
):
    '''
    Calcola hash ricorsivi di una cartella
    '''
    manifest: Manifest = hashing_utils.create_manifest(directory_path, algorithm)
    output_utils.display_manifest(manifest.directory, algorithm, manifest.directory_hash, manifest.file_count)

@app.command()
def dir_compare(
    directory1: Path = typer.Argument(..., exists=True, file_okay=False, dir_okay=True),
    directory2: Path = typer.Argument(..., exists=True, file_okay=False, dir_okay=True),
    algorithm: Algorithm = typer.Option(Algorithm.blake2b, "--algorithm", "-a", prompt=True),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Display detailed information about the differences")
):
    '''
    Confronta gli hash di due cartelle
    '''
    manifest1: Manifest = hashing_utils.create_manifest(directory1, algorithm)
    manifest2: Manifest = hashing_utils.create_manifest(directory2, algorithm)

    if hashing_utils.compare_manifests(manifest1, manifest2):
        output_utils.display_successful_dir_comparison(directory1, directory2, algorithm.value, manifest1.directory_hash)
    else:
        comparison: ManifestComparison = hashing_utils.compare_directories(manifest1, manifest2)
        output_utils.display_failed_dir_comparison(directory1, directory2, algorithm.value, comparison, verbose)

@app.command()
def algorithms():
    '''
    Mostra gli algoritmi disponibili
    '''
    output_utils.display_algorithm()