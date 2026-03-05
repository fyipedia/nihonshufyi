"""Command-line interface for nihonshufyi.

Requires the ``cli`` extra: ``pip install nihonshufyi[cli]``

Usage::

    nihonshufyi search "junmai daiginjo"
"""

from __future__ import annotations

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(
    name="nihonshufyi",
    help="Sake knowledge API client — search sake grades, breweries, and terms from NihonshuFYI.",
    no_args_is_help=True,
)
console = Console()


@app.command()
def search(
    query: str = typer.Argument(help="Search term (e.g. 'junmai daiginjo', 'niigata')"),
) -> None:
    """Search sakes, breweries, and glossary terms."""
    from nihonshufyi.api import NihonshuFYI

    with NihonshuFYI() as api:
        results = api.search(query)

    table = Table(title=f"Search: {query}")
    table.add_column("Type", style="cyan", no_wrap=True)
    table.add_column("Name")
    table.add_column("Detail")

    items = results.get("results", [])
    if not items:
        console.print(f"[yellow]No results found for '{query}'[/yellow]")
        return

    for item in items:
        item_type = item.get("type", "unknown")
        name = item.get("name", item.get("title", ""))
        detail = item.get("description", item.get("slug", ""))
        table.add_row(item_type, str(name), str(detail))

    console.print(table)


if __name__ == "__main__":
    app()
