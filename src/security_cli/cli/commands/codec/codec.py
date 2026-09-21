import typer
from .registry import CODEC
from .algorithm import EncodeAlgorithm as Algorithm
from .output import print_codec_result
import typer

app = typer.Typer()

@app.command()
def encode(
    text: str = typer.Option(..., "--text", "-t", prompt=True),
    algorithm: Algorithm = typer.Option(Algorithm.base64, "--algorithm", "-a", prompt=True)
):
    '''
    Codifica un testo in base all'algoritmo specificato.
    '''
    codec = CODEC[algorithm]
    encoded_text = codec.encode(text)
    print_codec_result(algorithm.value, "Encode", text, encoded_text)

@app.command()
def decode(
    text: str = typer.Option(..., "--text", "-t", prompt=True),
    algorithm: Algorithm = typer.Option(Algorithm.base64, "--algorithm", "-a", prompt=True)
):
    '''
    Decodifica un testo in base all'algoritmo specificato.
    '''
    codec = CODEC[algorithm]
    decoded_text = codec.decode(text)
    print_codec_result(algorithm.value, "Decode", text, decoded_text)