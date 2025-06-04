"""Setup configuration for Apple Documentation Scraper."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="apple-doc-scraper",
    version="0.1.0",
    author="Apple Documentation Scraper Team",
    description="Comprehensive scraper for Apple Developer Documentation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/apple-doc-scraper",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Documentation",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.11",
    install_requires=[
        "httpx>=0.27.0",
        "beautifulsoup4>=4.12.3",
        "markdownify>=0.12.1",
        "pyppeteer>=2.0.0",
        "asyncio-throttle>=1.0.2",
        "jsonschema>=4.21.1",
        "structlog>=24.1.0",
        "rich>=13.7.0",
        "click>=8.1.0",
    ],
    extras_require={
        "dev": [
            "mypy>=1.8.0",
            "pytest>=8.0.0",
            "pytest-asyncio>=0.23.5",
            "pytest-cov>=4.1.0",
            "black>=24.1.1",
            "ruff>=0.2.1",
            "types-beautifulsoup4>=4.12.0.20240229",
            "types-requests>=2.31.0.20240218",
        ]
    },
    entry_points={
        "console_scripts": [
            "apple-scraper=scraper.main:main",
        ],
    },
)