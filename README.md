# nihonshufyi

Sake knowledge API client for developers — search sake grades, breweries, and terminology from [NihonshuFYI](https://nihonshufyi.com).

<p align="center">
  <img src="demo.gif" alt="nihonshufyi demo — sake API search and lookup" width="800">
</p>

## Install

```bash
pip install nihonshufyi[api]     # API client (httpx)
pip install nihonshufyi[cli]     # + CLI (typer, rich)
pip install nihonshufyi[mcp]     # + MCP server
pip install nihonshufyi[all]     # Everything
```

## Quick Start

```python
from nihonshufyi.api import NihonshuFYI

with NihonshuFYI() as api:
    results = api.search("junmai daiginjo")
    print(results)
```

## CLI

```bash
nihonshufyi search "junmai daiginjo"
nihonshufyi search "niigata"
nihonshufyi search "yamada nishiki"
```

## MCP Server

```bash
# Add to Claude Desktop config
python -m nihonshufyi.mcp_server
```

Tools: `sake_search`

## API Client

```python
from nihonshufyi.api import NihonshuFYI

with NihonshuFYI() as api:
    # Search sakes, breweries, glossary terms
    results = api.search("junmai daiginjo")
```

## Links

- [NihonshuFYI](https://nihonshufyi.com) — Sake encyclopedia with grades, breweries, and terminology
- [PyPI](https://pypi.org/project/nihonshufyi/)
- [GitHub](https://github.com/fyipedia/nihonshufyi)
- [FYIPedia](https://fyipedia.com) — Open-source developer tools ecosystem
