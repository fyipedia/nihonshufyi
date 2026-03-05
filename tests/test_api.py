"""Tests for nihonshufyi.api — client initialization and URL construction."""

from nihonshufyi.api import NihonshuFYI


class TestNihonshuFYIInit:
    def test_default_base_url(self) -> None:
        client = NihonshuFYI()
        assert str(client._client.base_url) == "https://nihonshufyi.com"
        client.close()

    def test_custom_base_url(self) -> None:
        client = NihonshuFYI(base_url="https://example.com")
        assert str(client._client.base_url) == "https://example.com"
        client.close()

    def test_default_timeout(self) -> None:
        client = NihonshuFYI()
        assert client._client.timeout.connect == 10.0
        client.close()

    def test_custom_timeout(self) -> None:
        client = NihonshuFYI(timeout=30.0)
        assert client._client.timeout.connect == 30.0
        client.close()

    def test_context_manager(self) -> None:
        with NihonshuFYI() as api:
            assert str(api._client.base_url) == "https://nihonshufyi.com"


class TestURLConstruction:
    def test_search_url(self) -> None:
        client = NihonshuFYI()
        request = client._client.build_request("GET", "/api/search/", params={"q": "junmai"})
        assert "/api/search/" in str(request.url)
        assert "q=junmai" in str(request.url)
        client.close()
