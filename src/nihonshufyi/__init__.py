"""nihonshufyi — Sake knowledge API client for developers.

Search sake grades, breweries, and terminology from NihonshuFYI.

Usage::

    from nihonshufyi.api import NihonshuFYI

    with NihonshuFYI() as api:
        results = api.search("junmai daiginjo")
        print(results)
"""

__version__ = "0.1.0"
