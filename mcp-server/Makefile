.PHONY: help install test validate index server clean monitor test-index test-recovery index-force index-verify

help:
	@echo "Apple Docs MCP Server - Available commands:"
	@echo "  make install      - Install dependencies"
	@echo "  make test         - Run all tests"
	@echo "  make test-index   - Test indexing with sample docs"
	@echo "  make test-recovery - Test recovery from interruption"
	@echo "  make validate     - Validate documentation"
	@echo "  make index        - Build vector index (Task 02)"
	@echo "  make index-force  - Force rebuild entire index"
	@echo "  make index-verify - Verify index after building"
	@echo "  make monitor      - Monitor indexing progress"
	@echo "  make server       - Run MCP server (Task 04)"
	@echo "  make clean        - Clean temporary files"

install:
	python3 -m pip install -r requirements.txt

test:
	python tests/test_embeddings.py
	python tests/test_chromadb.py
	python tests/test_build_index.py

test-index:
	python tests/test_build_index.py

test-recovery:
	python scripts/test_recovery.py

validate:
	python scripts/validate_docs.py

index:
	python3 scripts/build_index_voyage.py

index-force:
	python3 scripts/build_index_voyage.py --force

index-verify:
	python3 scripts/build_index_voyage.py --verify

# Legacy TEI-based indexing
index-tei:
	python3 scripts/build_index.py

monitor:
	python3 scripts/monitor_indexing.py

server:
	python3 server/mcp_server.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf vectorstore/test*
	rm -rf temp_test*
	rm -rf .pytest_cache