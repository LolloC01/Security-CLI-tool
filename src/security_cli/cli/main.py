# Copyright (c) 2026 Lorenzo Colitto
# Questo codice è distribuito sotto i termini della licenza MIT.
# Vedi il file LICENSE nella radice del progetto per il testo completo.

import typer
from .commands.hashing.hash import app as hash_app

app = typer.Typer(
    name="appsec",
    help="Application Security Toolkit",
    no_args_is_help=True,
)

app.add_typer(
    hash_app,
    name="hash",
)

if __name__ == "__main__":
    app()