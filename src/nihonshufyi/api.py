"""HTTP API client for nihonshufyi.com REST endpoints.

Requires the ``api`` extra: ``pip install nihonshufyi[api]``

Usage::

    from nihonshufyi.api import NihonshuFYI

    with NihonshuFYI() as api:
        items = api.list_breweries()
        detail = api.get_brewery("example-slug")
        results = api.search("query")
"""

from __future__ import annotations

from typing import Any

import httpx


class NihonshuFYI:
    """API client for the nihonshufyi.com REST API.

    Provides typed access to all nihonshufyi.com endpoints including
    list, detail, and search operations.

    Args:
        base_url: API base URL. Defaults to ``https://nihonshufyi.com``.
        timeout: Request timeout in seconds. Defaults to ``10.0``.
    """

    def __init__(
        self,
        base_url: str = "https://nihonshufyi.com",
        timeout: float = 10.0,
    ) -> None:
        self._client = httpx.Client(base_url=base_url, timeout=timeout)

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        resp = self._client.get(
            path,
            params={k: v for k, v in params.items() if v is not None},
        )
        resp.raise_for_status()
        result: dict[str, Any] = resp.json()
        return result

    # -- Endpoints -----------------------------------------------------------

    def list_breweries(self, **params: Any) -> dict[str, Any]:
        """List all breweries."""
        return self._get("/api/v1/breweries/", **params)

    def get_brewery(self, slug: str) -> dict[str, Any]:
        """Get brewery by slug."""
        return self._get(f"/api/v1/breweries/" + slug + "/")

    def list_faqs(self, **params: Any) -> dict[str, Any]:
        """List all faqs."""
        return self._get("/api/v1/faqs/", **params)

    def get_faq(self, slug: str) -> dict[str, Any]:
        """Get faq by slug."""
        return self._get(f"/api/v1/faqs/" + slug + "/")

    def list_glossary(self, **params: Any) -> dict[str, Any]:
        """List all glossary."""
        return self._get("/api/v1/glossary/", **params)

    def get_term(self, slug: str) -> dict[str, Any]:
        """Get term by slug."""
        return self._get(f"/api/v1/glossary/" + slug + "/")

    def list_glossary_categories(self, **params: Any) -> dict[str, Any]:
        """List all glossary categories."""
        return self._get("/api/v1/glossary-categories/", **params)

    def get_glossary_category(self, slug: str) -> dict[str, Any]:
        """Get glossary category by slug."""
        return self._get(f"/api/v1/glossary-categories/" + slug + "/")

    def list_grades(self, **params: Any) -> dict[str, Any]:
        """List all grades."""
        return self._get("/api/v1/grades/", **params)

    def get_grade(self, slug: str) -> dict[str, Any]:
        """Get grade by slug."""
        return self._get(f"/api/v1/grades/" + slug + "/")

    def list_guides(self, **params: Any) -> dict[str, Any]:
        """List all guides."""
        return self._get("/api/v1/guides/", **params)

    def get_guide(self, slug: str) -> dict[str, Any]:
        """Get guide by slug."""
        return self._get(f"/api/v1/guides/" + slug + "/")

    def list_prefectures(self, **params: Any) -> dict[str, Any]:
        """List all prefectures."""
        return self._get("/api/v1/prefectures/", **params)

    def get_prefecture(self, slug: str) -> dict[str, Any]:
        """Get prefecture by slug."""
        return self._get(f"/api/v1/prefectures/" + slug + "/")

    def list_rice(self, **params: Any) -> dict[str, Any]:
        """List all rice."""
        return self._get("/api/v1/rice/", **params)

    def get_rice(self, slug: str) -> dict[str, Any]:
        """Get rice by slug."""
        return self._get(f"/api/v1/rice/" + slug + "/")

    def list_sake(self, **params: Any) -> dict[str, Any]:
        """List all sake."""
        return self._get("/api/v1/sake/", **params)

    def get_sake(self, slug: str) -> dict[str, Any]:
        """Get sake by slug."""
        return self._get(f"/api/v1/sake/" + slug + "/")

    def list_serving(self, **params: Any) -> dict[str, Any]:
        """List all serving."""
        return self._get("/api/v1/serving/", **params)

    def get_serving(self, slug: str) -> dict[str, Any]:
        """Get serving by slug."""
        return self._get(f"/api/v1/serving/" + slug + "/")

    def list_tools(self, **params: Any) -> dict[str, Any]:
        """List all tools."""
        return self._get("/api/v1/tools/", **params)

    def get_tool(self, slug: str) -> dict[str, Any]:
        """Get tool by slug."""
        return self._get(f"/api/v1/tools/" + slug + "/")

    def list_yeast(self, **params: Any) -> dict[str, Any]:
        """List all yeast."""
        return self._get("/api/v1/yeast/", **params)

    def get_yeast(self, slug: str) -> dict[str, Any]:
        """Get yeast by slug."""
        return self._get(f"/api/v1/yeast/" + slug + "/")

    def search(self, query: str, **params: Any) -> dict[str, Any]:
        """Search across all content."""
        return self._get(f"/api/v1/search/", q=query, **params)

    # -- Lifecycle -----------------------------------------------------------

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> NihonshuFYI:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
