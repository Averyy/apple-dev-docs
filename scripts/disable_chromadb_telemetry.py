#!/usr/bin/env python3
"""
Set environment variable to disable ChromaDB telemetry
"""

import os

# Add this to your .env file or set before running scripts
print("To disable ChromaDB telemetry warnings, add this to your environment:")
print("\nexport ANONYMIZED_TELEMETRY=false")
print("\nOr add to your .env file:")
print("ANONYMIZED_TELEMETRY=false")
print("\nYou can also set it in your shell profile (~/.zshrc or ~/.bash_profile)")