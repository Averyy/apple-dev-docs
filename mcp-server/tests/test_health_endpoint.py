#!/usr/bin/env python3
"""
Unit tests for health endpoint and related functions.

These tests call actual code and verify real behavior.
"""

import pytest
from unittest.mock import MagicMock, patch
from pathlib import Path
import tempfile
import os
from datetime import datetime, timezone


class MockDocument:
    """Mock Meilisearch Document object (has __iter__ but no .get())."""
    def __init__(self, data: dict):
        for key, value in data.items():
            setattr(self, key, value)

    def __iter__(self):
        return iter(self.__dict__.items())


class MockStats:
    """Mock Meilisearch stats response."""
    def __init__(self, number_of_documents=0, is_indexing=False):
        self.number_of_documents = number_of_documents
        self.is_indexing = is_indexing


class TestGetIndexMetadata:
    """Test get_index_metadata function."""

    @patch('apple_docs_mcp.meili_client')
    def test_converts_document_to_dict(self, mock_client):
        """Must convert Meilisearch Document to dict (Document has no .get())."""
        mock_index = MagicMock()
        mock_index.get_document.return_value = MockDocument({
            "id": "index_metadata",
            "last_indexed": "2026-01-10T12:00:00Z"
        })
        mock_client.index.return_value = mock_index

        from apple_docs_mcp import get_index_metadata
        result = get_index_metadata()

        # Key test: result must support .get() which Document doesn't have
        assert result.get("last_indexed") == "2026-01-10T12:00:00Z"
        assert result.get("nonexistent") is None  # .get() with default

    @patch('apple_docs_mcp.meili_client', None)
    def test_returns_none_without_client(self):
        """Returns None when Meilisearch unavailable."""
        from apple_docs_mcp import get_index_metadata
        assert get_index_metadata() is None


class TestHealthEndpoint:
    """Test the actual health endpoint behavior."""

    @pytest.mark.asyncio
    async def test_healthy_when_docs_above_threshold(self):
        """Status is 'healthy' only when docs >= MINIMUM_EXPECTED_DOCS."""
        from apple_docs_mcp import MINIMUM_EXPECTED_DOCS

        with patch('apple_docs_mcp.meili_index') as mock_index, \
             patch('apple_docs_mcp.meili_client') as mock_client, \
             patch('apple_docs_mcp.get_index_metadata') as mock_meta:

            # Exactly at threshold should be healthy
            mock_index.get_stats.return_value = MockStats(
                number_of_documents=MINIMUM_EXPECTED_DOCS,
                is_indexing=False
            )
            mock_index.search.return_value = {"facetDistribution": {"framework": {"SwiftUI": 100}}}
            mock_client.get_tasks.return_value = MagicMock(results=[])
            mock_meta.return_value = None

            from apple_docs_mcp import health_check
            response = await health_check(MagicMock())

            assert response.status_code == 200
            import json
            body = json.loads(response.body)
            assert body["status"] == "healthy"
            assert body["documents"] == MINIMUM_EXPECTED_DOCS

    @pytest.mark.asyncio
    async def test_degraded_when_docs_below_threshold(self):
        """Status is 'degraded' when docs < MINIMUM_EXPECTED_DOCS."""
        from apple_docs_mcp import MINIMUM_EXPECTED_DOCS

        with patch('apple_docs_mcp.meili_index') as mock_index, \
             patch('apple_docs_mcp.meili_client') as mock_client, \
             patch('apple_docs_mcp.get_index_metadata') as mock_meta:

            # One below threshold should be degraded
            docs_count = MINIMUM_EXPECTED_DOCS - 1
            mock_index.get_stats.return_value = MockStats(
                number_of_documents=docs_count,
                is_indexing=False
            )
            mock_index.search.return_value = {"facetDistribution": {"framework": {}}}
            mock_client.get_tasks.return_value = MagicMock(results=[])
            mock_meta.return_value = None

            from apple_docs_mcp import health_check
            response = await health_check(MagicMock())

            assert response.status_code == 503
            import json
            body = json.loads(response.body)
            assert body["status"] == "degraded"
            assert body["documents"] == docs_count

    @pytest.mark.asyncio
    async def test_indexing_takes_priority_over_degraded(self):
        """'indexing' status takes priority even when docs are low."""
        from apple_docs_mcp import MINIMUM_EXPECTED_DOCS

        with patch('apple_docs_mcp.meili_index') as mock_index, \
             patch('apple_docs_mcp.meili_client') as mock_client, \
             patch('apple_docs_mcp.get_index_metadata') as mock_meta:

            # Low docs but actively indexing
            mock_index.get_stats.return_value = MockStats(
                number_of_documents=50000,  # Way below threshold
                is_indexing=True
            )
            mock_index.search.return_value = {"facetDistribution": {"framework": {}}}
            mock_client.get_tasks.return_value = MagicMock(results=[])
            mock_meta.return_value = None

            from apple_docs_mcp import health_check
            response = await health_check(MagicMock())

            import json
            body = json.loads(response.body)
            # Should be "indexing" NOT "degraded" even though docs < threshold
            assert body["status"] == "indexing"
            assert body["is_indexing"] is True
            assert "progress" in body

    @pytest.mark.asyncio
    async def test_unhealthy_when_meilisearch_disconnected(self):
        """'unhealthy' when meili_index is None."""
        with patch('apple_docs_mcp.meili_index', None):
            from apple_docs_mcp import health_check
            response = await health_check(MagicMock())

            assert response.status_code == 503
            import json
            body = json.loads(response.body)
            assert body["status"] == "unhealthy"
            assert body["meilisearch"] == "disconnected"

    @pytest.mark.asyncio
    async def test_timestamps_come_from_actual_sources(self):
        """Verify timestamps are passed through from their actual sources."""
        from apple_docs_mcp import MINIMUM_EXPECTED_DOCS

        test_docs_updated = "2026-01-20T08:26:12Z"
        test_last_indexed = "2026-01-21T16:10:00Z"
        test_last_index_full = "2026-01-14T08:00:00Z"
        test_build_time = "2026-01-21T16:05:38Z"

        with patch('apple_docs_mcp.meili_index') as mock_index, \
             patch('apple_docs_mcp.meili_client') as mock_client, \
             patch('apple_docs_mcp.get_index_metadata') as mock_meta, \
             patch('apple_docs_mcp.DOCS_UPDATED', test_docs_updated), \
             patch('apple_docs_mcp.BUILD_TIME', test_build_time):

            mock_index.get_stats.return_value = MockStats(
                number_of_documents=MINIMUM_EXPECTED_DOCS,
                is_indexing=False
            )
            mock_index.search.return_value = {"facetDistribution": {"framework": {"SwiftUI": 100}}}
            mock_client.get_tasks.return_value = MagicMock(results=[])

            # Metadata contains last_indexed and last_index_full from Meilisearch
            mock_meta.return_value = {
                "last_indexed": test_last_indexed,
                "last_index_full": test_last_index_full
            }

            from apple_docs_mcp import health_check
            response = await health_check(MagicMock())

            import json
            body = json.loads(response.body)

            # Verify values come from the mocked sources
            assert body["docs_updated"] == test_docs_updated
            assert body["last_indexed"] == test_last_indexed
            assert body["last_index_full"] == test_last_index_full
            assert body["image_built"] == test_build_time

    @pytest.mark.asyncio
    async def test_timestamps_omitted_when_sources_empty(self):
        """Timestamps should NOT appear if source returns None/unknown."""
        from apple_docs_mcp import MINIMUM_EXPECTED_DOCS

        with patch('apple_docs_mcp.meili_index') as mock_index, \
             patch('apple_docs_mcp.meili_client') as mock_client, \
             patch('apple_docs_mcp.get_index_metadata') as mock_meta, \
             patch('apple_docs_mcp.DOCS_UPDATED', "unknown"), \
             patch('apple_docs_mcp.BUILD_TIME', "unknown"):

            mock_index.get_stats.return_value = MockStats(
                number_of_documents=MINIMUM_EXPECTED_DOCS,
                is_indexing=False
            )
            mock_index.search.return_value = {"facetDistribution": {"framework": {"SwiftUI": 100}}}
            mock_client.get_tasks.return_value = MagicMock(results=[])
            mock_meta.return_value = None  # No metadata

            from apple_docs_mcp import health_check
            response = await health_check(MagicMock())

            import json
            body = json.loads(response.body)

            # These should NOT be in response
            assert "docs_updated" not in body
            assert "last_indexed" not in body
            assert "last_index_full" not in body
            assert "image_built" not in body

    @pytest.mark.asyncio
    async def test_progress_percentage_calculated_correctly(self):
        """Progress should be (current_docs / expected_docs) * 100."""
        from apple_docs_mcp import EXPECTED_FULL_INDEX_SIZE

        with patch('apple_docs_mcp.meili_index') as mock_index, \
             patch('apple_docs_mcp.meili_client') as mock_client, \
             patch('apple_docs_mcp.get_index_metadata') as mock_meta:

            # 50% of expected docs
            half_docs = EXPECTED_FULL_INDEX_SIZE // 2
            mock_index.get_stats.return_value = MockStats(
                number_of_documents=half_docs,
                is_indexing=True
            )
            mock_index.search.return_value = {"facetDistribution": {"framework": {}}}
            mock_client.get_tasks.return_value = MagicMock(results=[])
            mock_meta.return_value = None

            from apple_docs_mcp import health_check
            response = await health_check(MagicMock())

            import json
            body = json.loads(response.body)

            # Should be approximately 50%
            assert body["progress"] == "50%"


class TestConfiguration:
    """Test configuration is read correctly from environment."""

    def test_minimum_docs_defaults_to_290k(self):
        """Without env var, MINIMUM_EXPECTED_DOCS should be 290000 (~90% of corpus)."""
        with patch.dict(os.environ, {}, clear=False):
            env_val = os.environ.pop("MIN_EXPECTED_DOCS", None)
            try:
                import importlib
                import apple_docs_mcp
                importlib.reload(apple_docs_mcp)
                assert apple_docs_mcp.MINIMUM_EXPECTED_DOCS == 290000
            finally:
                if env_val:
                    os.environ["MIN_EXPECTED_DOCS"] = env_val

    def test_minimum_docs_reads_from_env(self):
        """MIN_EXPECTED_DOCS env var should override default."""
        with patch.dict(os.environ, {"MIN_EXPECTED_DOCS": "150000"}):
            import importlib
            import apple_docs_mcp
            importlib.reload(apple_docs_mcp)
            assert apple_docs_mcp.MINIMUM_EXPECTED_DOCS == 150000

    def test_build_time_defaults_to_unknown(self):
        """Without env var, BUILD_TIME should be 'unknown'."""
        with patch.dict(os.environ, {}, clear=False):
            env_val = os.environ.pop("BUILD_TIME", None)
            try:
                import importlib
                import apple_docs_mcp
                importlib.reload(apple_docs_mcp)
                assert apple_docs_mcp.BUILD_TIME == "unknown"
            finally:
                if env_val:
                    os.environ["BUILD_TIME"] = env_val

    def test_build_time_reads_from_env(self):
        """BUILD_TIME env var should be used."""
        test_time = "2026-01-21T12:00:00Z"
        with patch.dict(os.environ, {"BUILD_TIME": test_time}):
            import importlib
            import apple_docs_mcp
            importlib.reload(apple_docs_mcp)
            assert apple_docs_mcp.BUILD_TIME == test_time

    def test_docs_updated_defaults_to_unknown(self):
        """Without env var, DOCS_UPDATED should be 'unknown'."""
        with patch.dict(os.environ, {}, clear=False):
            env_val = os.environ.pop("DOCS_UPDATED", None)
            try:
                import importlib
                import apple_docs_mcp
                importlib.reload(apple_docs_mcp)
                assert apple_docs_mcp.DOCS_UPDATED == "unknown"
            finally:
                if env_val:
                    os.environ["DOCS_UPDATED"] = env_val

    def test_docs_updated_reads_from_env(self):
        """DOCS_UPDATED env var should be used."""
        test_time = "2026-01-20T08:26:12Z"
        with patch.dict(os.environ, {"DOCS_UPDATED": test_time}):
            import importlib
            import apple_docs_mcp
            importlib.reload(apple_docs_mcp)
            assert apple_docs_mcp.DOCS_UPDATED == test_time


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
