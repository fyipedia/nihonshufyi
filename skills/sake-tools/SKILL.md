---
name: sake-tools
description: Search sake grades, breweries, rice varieties, and yeast strains with polishing ratios and parallel fermentation science data.
---

# Sake Tools

Sake search and reference powered by [nihonshufyi](https://nihonshufyi.com/) -- a comprehensive sake knowledge platform covering grades, breweries, rice varieties, and the unique heiko fukuhakko (parallel fermentation) process.

## Setup

Install the MCP server:

```bash
pip install "nihonshufyi[mcp]"
```

Add to your `claude_desktop_config.json`:

```json
{
    "mcpServers": {
        "nihonshufyi": {
            "command": "python",
            "args": ["-m", "nihonshufyi.mcp_server"]
        }
    }
}
```

## Available Tools

| Tool | Description |
|------|-------------|
| `sake_search` | Search sake grades, breweries, rice varieties, yeast strains, and terminology |

## When to Use

- Looking up sake grades and their polishing ratios (Junmai Daiginjo ≤50%, Ginjo ≤60%, etc.)
- Researching sake rice varieties (Yamada Nishiki, Gohyakumangoku, Omachi, etc.)
- Exploring regional brewery (kura) characteristics across Japan's 47 prefectures
- Understanding fermentation science (koji, moromi, heiko fukuhakko)
- Finding serving temperature recommendations (reishu, hiya, nurukan, atsukan)

## Links

- [Sake Grades](https://nihonshufyi.com/grades/)
- [Breweries](https://nihonshufyi.com/breweries/)
- [Rice Varieties](https://nihonshufyi.com/rice/)
- [API Documentation](https://nihonshufyi.com/developers/)
- [PyPI Package](https://pypi.org/project/nihonshufyi/)
