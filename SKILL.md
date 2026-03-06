---
name: sake-tools
description: Search 80 sake expressions, 10 rice varieties, 50 breweries, and sake terminology from NihonshuFYI. Use when answering questions about sake grades, polishing ratios, brewing process, or Japanese rice wine.
license: MIT
metadata:
  author: fyipedia
  version: "0.1.1"
  homepage: "https://nihonshufyi.com/"
---

# NihonshuFYI -- Sake Tools for AI Agents

Japanese sake knowledge API client for Python. Search 80 sake expressions, 10 rice varieties, 50 breweries, and sake terminology from NihonshuFYI -- the comprehensive sake reference with 101 expert guides covering the tokutei meishoshu classification system, polishing ratios, koji cultivation, and parallel multiple fermentation.

**Install**: `pip install nihonshufyi[api]` -- **Web**: [nihonshufyi.com](https://nihonshufyi.com/) -- **API**: [REST API](https://nihonshufyi.com/developers/) -- **PyPI**: [nihonshufyi](https://pypi.org/project/nihonshufyi/)

## When to Use

- User asks about sake grades (junmai, ginjo, daiginjo) or classification system
- User needs polishing ratio (seimaibuai) explanations
- User wants brewery profiles or regional sake characteristics
- User asks about sake rice varieties (Yamada Nishiki, Gohyakumangoku)
- User needs sake terminology (SMV, koji, moromi, nama, genshu)

## Tools

### `NihonshuFYI` API Client

HTTP client for the nihonshufyi.com REST API. Requires `pip install nihonshufyi[api]`.

```python
from nihonshufyi.api import NihonshuFYI

with NihonshuFYI() as api:
    results = api.search("junmai daiginjo")  # Search sake, breweries, rice, glossary
```

**Methods:**
- `search(query: str) -> dict` -- Search sakes, breweries, and glossary terms

## REST API (No Auth Required)

```bash
# Search
curl "https://nihonshufyi.com/api/v1/search/?q=junmai+daiginjo"

# Sake detail
curl "https://nihonshufyi.com/api/v1/sake/dassai-23/"

# Rice variety detail
curl "https://nihonshufyi.com/api/v1/rice/yamada-nishiki/"

# Brewery detail
curl "https://nihonshufyi.com/api/v1/breweries/asahi-shuzo/"

# Glossary term
curl "https://nihonshufyi.com/api/v1/glossary/koji/"

# Compare two sakes
curl "https://nihonshufyi.com/api/v1/compare/dassai-23/kubota-manju/"
```

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/sake/` | List all 80 sake expressions |
| GET | `/api/v1/sake/{slug}/` | Sake detail with grade, tasting notes |
| GET | `/api/v1/rice/` | List all 10 sake rice varieties |
| GET | `/api/v1/rice/{slug}/` | Rice variety detail with characteristics |
| GET | `/api/v1/breweries/` | List all 50 breweries |
| GET | `/api/v1/breweries/{slug}/` | Brewery detail with history, location |
| GET | `/api/v1/glossary/{slug}/` | Glossary term definition |
| GET | `/api/v1/search/?q={query}` | Search across all content |
| GET | `/api/v1/compare/{slug1}/{slug2}/` | Compare two sake expressions |
| GET | `/api/v1/random/` | Random sake expression |
| GET | `/api/v1/openapi.json` | OpenAPI 3.1.0 specification |

Full spec: [OpenAPI 3.1.0](https://nihonshufyi.com/api/v1/openapi.json)

## Sake Grade Classification (Tokutei Meishoshu)

| Grade | Polishing Ratio | Alcohol Added | Characteristics |
|-------|----------------|---------------|-----------------|
| Junmai Daiginjo | 50% or less | No | Pinnacle of sake craft, highly aromatic, elegant |
| Daiginjo | 50% or less | Yes (small) | Fragrant, refined, light body |
| Junmai Ginjo | 60% or less | No | Fruity, floral, balanced |
| Ginjo | 60% or less | Yes (small) | Aromatic, crisp, delicate |
| Tokubetsu Junmai | 60% or less | No | Rice character, umami, fuller body |
| Tokubetsu Honjozo | 60% or less | Yes | Clean, light, versatile |
| Junmai | No requirement | No | Pure rice sake, wide range of styles |
| Honjozo | 70% or less | Yes | Light, smooth, approachable |

## Rice Polishing (Seimaibuai)

| Polishing | Remaining | Grade Level |
|-----------|-----------|-------------|
| 70% | 70% remains | Honjozo -- balanced, moderate complexity |
| 60% | 60% remains | Ginjo -- fruity esters, floral aromatics |
| 50% | 50% remains | Daiginjo -- highly aromatic, pure starch |
| 35-40% | 35-40% remains | Ultra-premium, extremely delicate |
| 23% | 23% remains | Extreme polishing (e.g., Dassai 23) |

## Sake Rice Varieties

| Variety | Origin | Character |
|---------|--------|-----------|
| Yamada Nishiki | Hyogo | "King of sake rice," large shinpaku, elegant |
| Gohyakumangoku | Niigata | Clean, crisp, tanrei karakuchi style |
| Miyama Nishiki | Nagano | Light, dry, cool-climate adapted |
| Omachi | Okayama | Oldest pure sake rice, rich, deep, umami |
| Hattan Nishiki | Hiroshima | Soft water compatible, mild, balanced |

## Key Sake Concepts

| Concept | Description |
|---------|-------------|
| Nihonshu-do (SMV) | Sake Meter Value: positive = dry, negative = sweet |
| Acidity (San-do) | Higher acidity = sharper, fuller mouthfeel |
| Koji | Aspergillus oryzae mold that converts starch to sugar |
| Nama | Unpasteurized sake, fresh and lively, must be refrigerated |
| Genshu | Undiluted, full strength, typically 17-20% ABV |
| Koshu | Aged sake, amber color, complex, nutty |
| Nigori | Coarsely filtered, creamy, sweet |
| Toji | Master brewer |

## Demo

![NihonshuFYI demo](https://raw.githubusercontent.com/fyipedia/nihonshufyi/main/demo.gif)

## Beverage FYI Family

Part of the [FYIPedia](https://fyipedia.com) ecosystem: [CocktailFYI](https://cocktailfyi.com), [VinoFYI](https://vinofyi.com), [BeerFYI](https://beerfyi.com), [BrewFYI](https://brewfyi.com), [WhiskeyFYI](https://whiskeyfyi.com), [TeaFYI](https://teafyi.com), [NihonshuFYI](https://nihonshufyi.com).
