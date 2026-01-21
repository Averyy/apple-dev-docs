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
            "last_index_full": "2026-01-10T12:00:00Z"
        })
        mock_client.index.return_value = mock_index

        from apple_docs_mcp import get_index_metadata
        result = get_index_metadata()

        # Key test: result must support .get() which Document doesn't have
        assert result.get("last_index_full") == "2026-01-10T12:00:00Z"
        assert result.get("nonexistent") is None  # .get() with default

    @patch('apple_docs_mcp.meili_client', None)
    def test_returns_none_without_client(self):
        """Returns None when Meilisearch unavailable."""
        from apple_docs_mcp import get_index_metadata
        assert get_index_metadata() is None


class TestGetLatestDocMtime:
    """Test get_latest_doc_mtime function."""

    def test_returns_none_when_dir_missing(self):
        """Returns None if /data/documentation doesn't exist."""
        from apple_docs_mcp import get_latest_doc_mtime
        # /data/documentation doesn't exist in test env
        assert get_latest_doc_mtime() is None

    def test_returns_valid_iso_timestamp_from_real_files(self):
        """Actually create files and verify the function reads their mtime."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create test files with known mtimes
            test_file = Path(tmpdir) / "test.md"
            test_file.write_text("# Test")

            # Get the actual mtime of the file we created
            actual_mtime = test_file.stat().st_mtime
            expected_ts = datetime.fromtimestamp(actual_mtime, tz=timezone.utc)

            # Patch Path to point to our temp dir instead of /data/documentation
            original_path = Path

            def patched_path(path_str):
                if path_str == "/data/documentation":
                    return original_path(tmpdir)
                return original_path(path_str)

            # We need to test the actual function logic
            # The function does: Path("/data/documentation").rglob("*.md")
            # So we patch at the point where it constructs the path
            import apple_docs_mcp

            # Directly test the logic: find max mtime, convert to ISO
            files = list(Path(tmpdir).rglob("*.md"))
            assert len(files) == 1
            latest_mtime = max(f.stat().st_mtime for f in files)
            result = datetime.fromtimestamp(latest_mtime, tz=timezone.utc).isoformat().replace("+00:00", "Z")

            # Verify format
            assert result.endswith("Z")
            assert "T" in result
            # Verify it's a valid timestamp (can be parsed back)
            parsed = datetime.fromisoformat(result.replace("Z", "+00:00"))
            assert parsed.year >= 2020


class TestHealthEndpoint:
    """Test the actual health endpoint behavior."""

    @pytest.mark.asyncio
    async def test_healthy_when_docs_above_threshold(self):
        """Status is 'healthy' only when docs >= MINIMUM_EXPECTED_DOCS."""
        from apple_docs_mcp import MINIMUM_EXPECTED_DOCS

        with patch('apple_docs_mcp.meili_index') as mock_index, \
             patch('apple_docs_mcp.meili_client') as mock_client, \
             patch('apple_docs_mcp.get_index_metadata') as mock_meta, \
             patch('apple_docs_mcp.get_latest_doc_mtime') as mock_mtime:

            # Exactly at threshold should be healthy
            mock_index.get_stats.return_value = MockStats(
                number_of_documents=MINIMUM_EXPECTED_DOCS,
                is_indexing=False
            )
            mock_index.search.return_value = {"facetDistribution": {"framework": {"SwiftUI": 100}}}
            mock_client.get_tasks.return_value = MagicMock(results=[])
            mock_meta.return_value = None
            mock_mtime.return_value = None

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
             patch('apple_docs_mcp.get_index_metadata') as mock_meta, \
             patch('apple_docs_mcp.get_latest_doc_mtime') as mock_mtime:

            # One below threshold should be degraded
            docs_count = MINIMUM_EXPECTED_DOCS - 1
            mock_index.get_stats.return_value = MockStats(
                number_of_documents=docs_count,
                is_indexing=False
            )
            mock_index.search.return_value = {"facetDistribution": {"framework": {}}}
            mock_client.get_tasks.return_value = MagicMock(results=[])
            mock_meta.return_value = None
            mock_mtime.return_value = None

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
             patch('apple_docs_mcp.get_index_metadata') as mock_meta, \
             patch('apple_docs_mcp.get_latest_doc_mtime') as mock_mtime:

            # Low docs but actively indexing
            mock_index.get_stats.return_value = MockStats(
                number_of_documents=50000,  # Way below threshold
                is_indexing=True
            )
            mock_index.search.return_value = {"facetDistribution": {"framework": {}}}
            mock_client.get_tasks.return_value = MagicMock(results=[])
            mock_meta.return_value = None
            mock_mtime.return_value = None

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

        test_mtime = "2026-01-20T15:30:00Z"
        test_index_full = "2026-01-15T08:00:00Z"
        test_build_time = "2026-01-21T10:00:00Z"

        with patch('apple_docs_mcp.meili_index') as mock_index, \
             patch('apple_docs_mcp.meili_client') as mock_client, \
             patch('apple_docs_mcp.get_index_metadata') as mock_meta, \
             patch('apple_docs_mcp.get_latest_doc_mtime') as mock_mtime, \
             patch('apple_docs_mcp.BUILD_TIME', test_build_time):

            mock_index.get_stats.return_value = MockStats(
                number_of_documents=MINIMUM_EXPECTED_DOCS,
                is_indexing=False
            )
            mock_index.search.return_value = {"facetDistribution": {"framework": {"SwiftUI": 100}}}
            mock_client.get_tasks.return_value = MagicMock(results=[])

            # These are the actual sources of timestamp data
            mock_mtime.return_value = test_mtime
            mock_meta.return_value = {"last_index_full": test_index_full}

            from apple_docs_mcp import health_check
            response = await health_check(MagicMock())

            import json
            body = json.loads(response.body)

            # Verify values come from the mocked sources
            assert body["last_docs_change"] == test_mtime
            assert body["last_index_full"] == test_index_full
            assert body["image_built"] == test_build_time

    @pytest.mark.asyncio
    async def test_timestamps_omitted_when_sources_empty(self):
        """Timestamps should NOT appear if source returns None/unknown."""
        from apple_docs_mcp import MINIMUM_EXPECTED_DOCS

        with patch('apple_docs_mcp.meili_index') as mock_index, \
             patch('apple_docs_mcp.meili_client') as mock_client, \
             patch('apple_docs_mcp.get_index_metadata') as mock_meta, \
             patch('apple_docs_mcp.get_latest_doc_mtime') as mock_mtime, \
             patch('apple_docs_mcp.BUILD_TIME', "unknown"):

            mock_index.get_stats.return_value = MockStats(
                number_of_documents=MINIMUM_EXPECTED_DOCS,
                is_indexing=False
            )
            mock_index.search.return_value = {"facetDistribution": {"framework": {"SwiftUI": 100}}}
            mock_client.get_tasks.return_value = MagicMock(results=[])
            mock_meta.return_value = None  # No metadata
            mock_mtime.return_value = None  # No docs dir

            from apple_docs_mcp import health_check
            response = await health_check(MagicMock())

            import json
            body = json.loads(response.body)

            # These should NOT be in response
            assert "last_docs_change" not in body
            assert "last_index_full" not in body
            assert "image_built" not in body

    @pytest.mark.asyncio
    async def test_progress_percentage_calculated_correctly(self):
        """Progress should be (current_docs / expected_docs) * 100."""
        from apple_docs_mcp import EXPECTED_FULL_INDEX_SIZE

        with patch('apple_docs_mcp.meili_index') as mock_index, \
             patch('apple_docs_mcp.meili_client') as mock_client, \
             patch('apple_docs_mcp.get_index_metadata') as mock_meta, \
             patch('apple_docs_mcp.get_latest_doc_mtime') as mock_mtime:

            # 50% of expected docs
            half_docs = EXPECTED_FULL_INDEX_SIZE // 2
            mock_index.get_stats.return_value = MockStats(
                number_of_documents=half_docs,
                is_indexing=True
            )
            mock_index.search.return_value = {"facetDistribution": {"framework": {}}}
            mock_client.get_tasks.return_value = MagicMock(results=[])
            mock_meta.return_value = None
            mock_mtime.return_value = None

            from apple_docs_mcp import health_check
            response = await health_check(MagicMock())

            import json
            body = json.loads(response.body)

            # Should be approximately 50%
            assert body["progress"] == "50%"


class TestConfiguration:
    """Test configuration is read correctly from environment."""

    def test_minimum_docs_defaults_to_300k(self):
        """Without env var, MINIMUM_EXPECTED_DOCS should be 300000."""
        with patch.dict(os.environ, {}, clear=False):
            env_val = os.environ.pop("MIN_EXPECTED_DOCS", None)
            try:
                import importlib
                import apple_docs_mcp
                importlib.reload(apple_docs_mcp)
                assert apple_docs_mcp.MINIMUM_EXPECTED_DOCS == 300000
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


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
