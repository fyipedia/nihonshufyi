"""MCP server for nihonshufyi — sake knowledge tools for AI assistants.

Requires the ``mcp`` extra: ``pip install nihonshufyi[mcp]``

Run as a standalone server::

    python -m nihonshufyi.mcp_server

Or configure in ``claude_desktop_config.json``::

    {
        "mcpServers": {
            "nihonshufyi": {
                "command": "python",
                "args": ["-m", "nihonshufyi.mcp_server"]
            }
        }
    }
"""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("nihonshufyi")


@mcp.tool()
def sake_search(query: str) -> str:
    """Search for sakes, breweries, and terminology on NihonshuFYI.

    Search across sake grades (junmai, daiginjo, honjozo), breweries,
    prefectures, rice varieties, yeast strains, serving temperatures,
    and glossary terms.

    Args:
        query: Search term (e.g. "junmai daiginjo", "niigata", "yamada nishiki").
    """
    from nihonshufyi.api import NihonshuFYI

    with NihonshuFYI() as api:
        results = api.search(query)

    items = results.get("results", [])
    if not items:
        return f"No results found for '{query}'."

    lines = [
        f"## Sake Search: {query}",
        "",
        f"Found {len(items)} result(s):",
        "",
        "| Type | Name | Detail |",
        "|------|------|--------|",
    ]

    for item in items:
        item_type = item.get("type", "unknown")
        name = item.get("name", item.get("title", ""))
        detail = item.get("description", item.get("slug", ""))
        lines.append(f"| {item_type} | {name} | {detail} |")

    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()
