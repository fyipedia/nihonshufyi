"""MCP server for nihonshufyi — AI assistant tools for nihonshufyi.com.

Run: uvx --from "nihonshufyi[mcp]" python -m nihonshufyi.mcp_server
"""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("NihonshuFYI")


@mcp.tool()
def list_sake(limit: int = 20, offset: int = 0) -> str:
    """List sake from nihonshufyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from nihonshufyi.api import NihonshuFYI

    with NihonshuFYI() as api:
        data = api.list_sake(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No sake found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def get_sake(slug: str) -> str:
    """Get detailed information about a specific sake.

    Args:
        slug: URL slug identifier for the sake.
    """
    from nihonshufyi.api import NihonshuFYI

    with NihonshuFYI() as api:
        data = api.get_sake(slug)
        return str(data)


@mcp.tool()
def list_breweries(limit: int = 20, offset: int = 0) -> str:
    """List breweries from nihonshufyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from nihonshufyi.api import NihonshuFYI

    with NihonshuFYI() as api:
        data = api.list_breweries(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No breweries found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def search_nihonshu(query: str) -> str:
    """Search nihonshufyi.com for sake, breweries, rice varieties, and grades.

    Args:
        query: Search query string.
    """
    from nihonshufyi.api import NihonshuFYI

    with NihonshuFYI() as api:
        data = api.search(query)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return f"No results found for \"{query}\"."
        items = results[:10] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


def main() -> None:
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
