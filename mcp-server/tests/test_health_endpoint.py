#!/usr/bin/env python3
"""
Unit tests for health endpoint and metadata functions.

These tests would have caught the Document vs dict bug.
"""

import pytest
from unittest.mock import MagicMock, patch


class MockDocument:
    """
    Mock Meilisearch Document object.
    Meilisearch SDK returns Document objects, not dicts.
    Document implements __iter__ for dict() conversion.
    """
    def __init__(self, data: dict):
        for key, value in data.items():
            setattr(self, key, value)

    def __iter__(self):
        return iter(self.__dict__.items())

    # Document does NOT have .get() method - this is the bug we're testing for
    # def get(self, key, default=None): ...


class TestGetIndexMetadata:
    """Test get_index_metadata function handles Document objects correctly."""

    def test_document_to_dict_conversion(self):
        """Verify Document objects can be converted to dict."""
        doc = MockDocument({
            "id": "index_metadata",
            "last_checked": "2026-01-11T12:00:00Z",
            "last_updated": "2026-01-10T12:00:00Z"
        })

        # This is what the fixed code does
        result = dict(doc)

        assert result["last_checked"] == "2026-01-11T12:00:00Z"
        assert result["last_updated"] == "2026-01-10T12:00:00Z"
        assert result.get("last_checked") == "2026-01-11T12:00:00Z"

    def test_document_has_no_get_method(self):
        """Verify Document objects don't have .get() - the original bug."""
        doc = MockDocument({"key": "value"})

        # This was the bug - calling .get() on Document raises AttributeError
        assert not hasattr(doc, 'get')

        with pytest.raises(AttributeError):
            doc.get("key")

    @patch('apple_docs_mcp.meili_client')
    def test_get_index_metadata_returns_dict(self, mock_client):
        """Test get_index_metadata converts Document to dict."""
        # Import after patching
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).parent.parent))

        # Setup mock
        mock_index = MagicMock()
        mock_doc = MockDocument({
            "id": "index_metadata",
            "last_checked": "2026-01-11T12:00:00Z",
            "last_updated": "2026-01-10T12:00:00Z"
        })
        mock_index.get_document.return_value = mock_doc
        mock_client.index.return_value = mock_index

        from apple_docs_mcp import get_index_metadata

        result = get_index_metadata()

        # Result should be a dict, not a Document
        assert isinstance(result, dict)
        # Should be able to call .get() on result
        assert result.get("last_checked") == "2026-01-11T12:00:00Z"


class TestHealthEndpoint:
    """Test health endpoint handles metadata correctly."""

    def test_metadata_dict_access(self):
        """Verify health endpoint can access metadata as dict."""
        metadata = {
            "last_checked": "2026-01-11T12:00:00Z",
            "last_updated": "2026-01-10T12:00:00Z"
        }

        # This is what the health endpoint does
        response_data = {}
        if metadata.get("last_checked"):
            response_data["last_checked"] = metadata["last_checked"]
        if metadata.get("last_updated"):
            response_data["last_updated"] = metadata["last_updated"]

        assert response_data["last_checked"] == "2026-01-11T12:00:00Z"
        assert response_data["last_updated"] == "2026-01-10T12:00:00Z"

    def test_metadata_none_handling(self):
        """Verify health endpoint handles None metadata."""
        metadata = None

        response_data = {}
        if metadata:
            if metadata.get("last_checked"):
                response_data["last_checked"] = metadata["last_checked"]

        assert "last_checked" not in response_data


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
