# nihonshufyi

[![PyPI version](https://agentgif.com/badge/pypi/nihonshufyi/version.svg)](https://pypi.org/project/nihonshufyi/)
[![Python](https://img.shields.io/pypi/pyversions/nihonshufyi)](https://pypi.org/project/nihonshufyi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Japanese sake knowledge API client for Python. Search 80 sake expressions, 10 rice varieties, 50 breweries, and sake terminology from [NihonshuFYI](https://nihonshufyi.com) -- the comprehensive sake reference with 101 expert guides covering the tokutei meishoshu classification system, polishing ratios, koji cultivation, and the art of parallel multiple fermentation.

> **Explore sake at [nihonshufyi.com](https://nihonshufyi.com)** -- [Sake Directory](https://nihonshufyi.com/sake/) | [Rice Varieties](https://nihonshufyi.com/rice/) | [Breweries](https://nihonshufyi.com/breweries/) | [Sake Guides](https://nihonshufyi.com/guides/)

<p align="center">
  <img src="https://raw.githubusercontent.com/fyipedia/nihonshufyi/main/demo.gif" alt="nihonshufyi demo -- sake API search and lookup" width="800">
</p>

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [What You'll Find on NihonshuFYI](#what-youll-find-on-nihonshufyi)
  - [Sake Grade Classification](#sake-grade-classification)
  - [Rice Polishing (Seimaibuai)](#rice-polishing-seimaibuai)
  - [The Brewing Process](#the-brewing-process)
  - [Sake Rice Varieties](#sake-rice-varieties)
  - [Key Sake Concepts](#key-sake-concepts)
- [API Endpoints](#api-endpoints)
- [Command-Line Interface](#command-line-interface)
- [MCP Server (Claude, Cursor, Windsurf)](#mcp-server-claude-cursor-windsurf)
- [API Client](#api-client)
- [Learn More About Sake](#learn-more-about-sake)
- [Beverage FYI Family](#beverage-fyi-family)
- [License](#license)

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
    # Search sake, breweries, rice varieties, glossary terms
    results = api.search("junmai daiginjo")
    print(results)

    # Look up a glossary term
    term = api.glossary_term("koji")
    print(term["definition"])
```

## What You'll Find on NihonshuFYI

NihonshuFYI is a comprehensive sake reference covering 80 sake expressions, 10 sake rice varieties, 50 breweries across Japan, and 101 expert guides. Nihonshu (the Japanese term for sake) is one of the world's most complex fermented beverages -- brewed through a unique process called parallel multiple fermentation where saccharification and alcohol fermentation occur simultaneously in the same vessel.

### Sake Grade Classification

The tokutei meishoshu (special designation sake) system classifies premium sake by two factors: polishing ratio and whether distilled alcohol is added. These 8 grades represent the top tier of sake production:

| Grade | Polishing Ratio | Alcohol Added | Characteristics |
|-------|----------------|---------------|-----------------|
| Junmai Daiginjo | 50% or less | No | Pinnacle of sake craft, highly aromatic, elegant |
| Daiginjo | 50% or less | Yes (small amount) | Fragrant, refined, light body |
| Junmai Ginjo | 60% or less | No | Fruity, floral, balanced |
| Ginjo | 60% or less | Yes (small amount) | Aromatic, crisp, delicate |
| Tokubetsu Junmai | 60% or less | No | Rice character, umami, fuller body |
| Tokubetsu Honjozo | 60% or less | Yes | Clean, light, versatile |
| Junmai | No requirement | No | Pure rice sake, wide range of styles |
| Honjozo | 70% or less | Yes | Light, smooth, approachable |

The "junmai" prefix means pure rice -- no distilled alcohol added. This does not inherently make it superior; small additions of brewer's alcohol can enhance aroma extraction and create lighter styles.

Learn more: [Sake Grade System](https://nihonshufyi.com/grade/) · [Sake Encyclopedia](https://nihonshufyi.com/sake/)

### Rice Polishing (Seimaibuai)

Polishing ratio (seimaibuai) is the percentage of the rice grain remaining after milling. The outer layers of rice contain proteins and fats that can produce off-flavors, so premium sake uses rice polished to remove these layers:

| Polishing | Remaining | Result |
|-----------|-----------|--------|
| 70% | 70% of grain remains | Honjozo level -- balanced, moderate complexity |
| 60% | 60% of grain remains | Ginjo level -- fruity esters, floral aromatics |
| 50% | 50% of grain remains | Daiginjo level -- highly aromatic, pure starch |
| 35-40% | 35-40% of grain remains | Ultra-premium, extremely delicate and refined |
| 23% | 23% of grain remains | Extreme polishing (e.g., Dassai 23), technical showcase |

Polishing from 70% to 50% removes approximately 40% more of the grain's mass, significantly increasing production cost and waste -- explaining the price premium of daiginjo-class sake.

Learn more: [Rice Polishing Guide](https://nihonshufyi.com/rice/) · [Sake Glossary](https://nihonshufyi.com/glossary/)

### The Brewing Process

Sake brewing (jozo) is fundamentally different from beer or wine production. Key stages:

| Stage | Japanese | Process |
|-------|----------|---------|
| Rice Polishing | Seimai | Mill rice to target polishing ratio |
| Washing & Soaking | Senmai / Shinseki | Precise water absorption control (seconds matter) |
| Steaming | Mushimai | Steam rice for koji and moromi |
| Koji Making | Seigiku | Inoculate steamed rice with Aspergillus oryzae mold (48-72 hours) |
| Starter Mash | Shubo / Moto | Concentrate yeast culture with koji, rice, water |
| Main Mash | Moromi | Three-stage addition (sandan jikomi) over 4 days |
| Fermentation | Hakko | 18-32 days at low temperature (parallel multiple fermentation) |
| Pressing | Joso | Separate sake from lees (assaku, fukurozuri, or arabashiri methods) |
| Pasteurization | Hi-ire | Heat to 60-65C (some sake skip this: nama) |

The parallel multiple fermentation is what makes sake unique: koji mold converts rice starch to sugar while yeast simultaneously converts that sugar to alcohol, achieving natural alcohol levels of 18-20% -- higher than any other fermented (not distilled) beverage.

Learn more: [Brewing Process Guide](https://nihonshufyi.com/process/) · [Sake Guides](https://nihonshufyi.com/guide/)

### Sake Rice Varieties

NihonshuFYI catalogs 10 sake-specific rice varieties (sakamai/shuzokotekimai). Sake rice differs from table rice: larger grains, prominent starch core (shinpaku), and lower protein content.

| Variety | Origin | Character | Notable Sake |
|---------|--------|-----------|-------------|
| Yamada Nishiki | Hyogo | "King of sake rice," large shinpaku, elegant | Dassai, many daiginjo |
| Gohyakumangoku | Niigata | Clean, crisp, tanrei karakuchi style | Kubota, Hakkaisan |
| Miyama Nishiki | Nagano | Light, dry, cool-climate adapted | Masumi |
| Omachi | Okayama | Oldest pure sake rice, rich, deep, umami | Takachiyo, specialty junmai |
| Hattan Nishiki | Hiroshima | Soft water compatible, mild, balanced | Kamoizumi |

Learn more: [Sake Rice Varieties](https://nihonshufyi.com/rice/) · [Brewery Profiles](https://nihonshufyi.com/brewery/)

### Key Sake Concepts

| Concept | Description |
|---------|-------------|
| Nihonshu-do (SMV) | Sake Meter Value: positive = dry, negative = sweet |
| Acidity (San-do) | Higher acidity = sharper, fuller mouthfeel |
| Amino Acid Level | Higher = more umami and richness |
| Nama (Unpasteurized) | Fresh, lively, must be refrigerated |
| Genshu (Undiluted) | Full strength, typically 17-20% ABV |
| Koshu (Aged) | Aged sake, amber color, complex, nutty |
| Nigori (Cloudy) | Coarsely filtered, creamy, sweet |
| Toji | Master brewer, traditionally seasonal craftspeople |

Learn more: [Sake Terminology](https://nihonshufyi.com/glossary/) · [Sake Comparison Tool](https://nihonshufyi.com/compare/)

## API Endpoints

All endpoints are free, require no authentication, and return JSON with CORS enabled.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/sake/` | List all 80 sake expressions |
| GET | `/api/v1/sake/{slug}/` | Sake detail with grade, tasting notes |
| GET | `/api/v1/rice/` | List all 10 sake rice varieties |
| GET | `/api/v1/rice/{slug}/` | Rice variety detail with characteristics |
| GET | `/api/v1/breweries/` | List all 50 breweries |
| GET | `/api/v1/breweries/{slug}/` | Brewery detail with history, location |
| GET | `/api/v1/glossary/` | List all sake terminology |
| GET | `/api/v1/glossary/{slug}/` | Glossary term definition |
| GET | `/api/v1/search/?q={query}` | Search across all content |
| GET | `/api/v1/compare/{slug1}/{slug2}/` | Compare two sake expressions |
| GET | `/api/v1/random/` | Random sake expression |
| GET | `/api/v1/guides/` | List all 101 guides |
| GET | `/api/v1/guides/{slug}/` | Guide detail |
| GET | `/api/v1/openapi.json` | OpenAPI 3.1.0 specification |

### Example

```bash
curl -s "https://nihonshufyi.com/api/v1/sake/dassai-23/"
```

```json
{
  "slug": "dassai-23",
  "name": "Dassai 23",
  "grade": "Junmai Daiginjo",
  "brewery": "Asahi Shuzo",
  "prefecture": "Yamaguchi",
  "rice": "Yamada Nishiki",
  "polishing_ratio": 23,
  "abv": 16.0,
  "smv": 4,
  "description": "Ultra-premium junmai daiginjo polished to an extraordinary 23%, showcasing exceptional purity, floral aromatics, and silky texture.",
  "tasting_notes": ["floral", "melon", "pear", "honey", "clean finish"],
  "url": "https://nihonshufyi.com/sake/dassai-23/"
}
```

Full API documentation: [nihonshufyi.com/developers/](https://nihonshufyi.com/developers/).
OpenAPI 3.1.0 spec: [nihonshufyi.com/api/v1/openapi.json](https://nihonshufyi.com/api/v1/openapi.json).

## Command-Line Interface

```bash
# Search sake, breweries, rice varieties
nihonshufyi search "junmai daiginjo"
nihonshufyi search "niigata"
nihonshufyi search "yamada nishiki"

# Look up sake terminology
nihonshufyi term "koji"
nihonshufyi term "seimaibuai"
nihonshufyi term "moromi"
```

The CLI displays results in formatted tables with rich terminal output.

## MCP Server (Claude, Cursor, Windsurf)

Run as an MCP server for AI-assisted sake queries:

```bash
python -m nihonshufyi.mcp_server
```

**Claude Desktop** (`~/.claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "nihonshufyi": {
      "command": "uvx",
      "args": ["--from", "nihonshufyi[mcp]", "python", "-m", "nihonshufyi.mcp_server"]
    }
  }
}
```

**Tools**: `sake_search`, `sake_glossary_term`

## API Client

```python
from nihonshufyi.api import NihonshuFYI

with NihonshuFYI() as api:
    # Search across sake, breweries, rice, glossary
    results = api.search("junmai daiginjo")

    # Look up sake terminology
    term = api.glossary_term("parallel-multiple-fermentation")
    print(term["definition"])

    # Compare two sake expressions
    comparison = api.compare("dassai-23", "kubota-manju")

    # Get a random sake
    random_sake = api.random()
```

## Learn More About Sake

- **Reference**: [Sake Directory](https://nihonshufyi.com/sake/) | [Rice Varieties](https://nihonshufyi.com/rice/) | [Breweries](https://nihonshufyi.com/breweries/)
- **Glossary**: [Sake Terminology](https://nihonshufyi.com/glossary/)
- **Guides**: [Sake Guides](https://nihonshufyi.com/guides/)
- **Compare**: [Sake Comparisons](https://nihonshufyi.com/compare/)
- **API**: [Developer Docs](https://nihonshufyi.com/developers/) | [OpenAPI Spec](https://nihonshufyi.com/api/v1/openapi.json)

## Beverage FYI Family

Part of the [FYIPedia](https://fyipedia.com) open-source developer tools ecosystem -- world beverages from cocktails to sake.

| Site | Domain | Focus |
|------|--------|-------|
| CocktailFYI | [cocktailfyi.com](https://cocktailfyi.com) | 636 cocktails, ABV, calories, flavor profiles |
| VinoFYI | [vinofyi.com](https://vinofyi.com) | Wines, grapes, regions, wineries, food pairings |
| BeerFYI | [beerfyi.com](https://beerfyi.com) | 112 beer styles, hops, malts, yeast, BJCP |
| BrewFYI | [brewfyi.com](https://brewfyi.com) | 72 coffee varieties, roasting, 21 brew methods |
| WhiskeyFYI | [whiskeyfyi.com](https://whiskeyfyi.com) | 80 whiskey expressions, distilleries, regions |
| TeaFYI | [teafyi.com](https://teafyi.com) | 60 tea varieties, teaware, brewing guides |
| **NihonshuFYI** | [nihonshufyi.com](https://nihonshufyi.com) | **80 sake, rice varieties, 50 breweries** |

## License

MIT
