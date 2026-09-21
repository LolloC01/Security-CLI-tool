from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def print_codec_result(
    algorithm: str,
    operation: str,
    input_text: str,
    output_text: str,
) -> None:

    table = Table(show_header=False, box=None)

    table.add_row("Algorithm", algorithm)
    table.add_row("Operation", operation)
    table.add_row("Input", input_text)
    table.add_row("Output", output_text)

    console.print(
        Panel(
            table,
            title="Encoding Result",
            border_style="green",
        )
    )