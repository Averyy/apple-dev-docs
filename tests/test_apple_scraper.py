"""Tests for Apple documentation scraper."""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from bs4 import BeautifulSoup

from scraper.apple_scraper import AppleDocumentationScraper


@pytest.fixture
def sample_html():
    """Sample Apple documentation HTML."""
    return """
    <html>
    <head>
        <title>Text | Apple Developer Documentation</title>
    </head>
    <body>
        <h1>Text</h1>
        <div class="abstract">
            A view that displays one or more lines of read-only text.
        </div>
        
        <section class="declaration">
            <pre><code class="language-swift">
struct Text : View {
    // Implementation
}
            </code></pre>
        </section>
        
        <section id="overview">
            <h2>Overview</h2>
            <p>Use Text to display strings in your app's UI.</p>
        </section>
        
        <section class="availability">
            <span class="badge">iOS 13.0+</span>
            <span class="badge">macOS 10.15+</span>
        </section>
    </body>
    </html>
    """


@pytest.mark.asyncio
async def test_extract_page_data(sample_html):
    """Test extracting data from a page."""
    scraper = AppleDocumentationScraper("swiftui")
    soup = BeautifulSoup(sample_html, 'html.parser')
    
    data = await scraper.extract_page_data(
        soup, 
        "https://developer.apple.com/documentation/swiftui/text"
    )
    
    assert data is not None
    assert data['title'] == 'Text'
    assert data['framework'] == 'Swiftui'
    assert data['brief_description'] == 'A view that displays one or more lines of read-only text.'
    assert 'swift' in data['declaration']
    assert 'struct Text : View' in data['declaration']['swift']


@pytest.mark.asyncio
async def test_is_valid_doc_url():
    """Test URL validation."""
    scraper = AppleDocumentationScraper("swiftui")
    
    # Valid URLs
    assert scraper._is_valid_doc_url("https://developer.apple.com/documentation/swiftui/text")
    assert scraper._is_valid_doc_url("https://developer.apple.com/documentation/swiftui/view/frame")
    
    # Invalid URLs
    assert not scraper._is_valid_doc_url("https://developer.apple.com/documentation/uikit/text")
    assert not scraper._is_valid_doc_url("https://example.com/documentation/swiftui/text")
    assert not scraper._is_valid_doc_url("https://developer.apple.com/documentation/swiftui/changes/")
    assert not scraper._is_valid_doc_url("https://developer.apple.com/documentation/swiftui/api.json")


@pytest.mark.asyncio
async def test_get_relative_path():
    """Test converting URLs to file paths."""
    scraper = AppleDocumentationScraper("swiftui")
    
    # Test various URL patterns
    assert scraper.get_relative_path(
        "https://developer.apple.com/documentation/swiftui/text"
    ).name == "text.md"
    
    assert scraper.get_relative_path(
        "https://developer.apple.com/documentation/swiftui/view/frame"
    ).name == "view_frame.md"
    
    assert scraper.get_relative_path(
        "https://developer.apple.com/documentation/swiftui/"
    ).name == "index.md"


@pytest.mark.asyncio
async def test_discover_urls():
    """Test URL discovery with mocked responses."""
    scraper = AppleDocumentationScraper("swiftui")
    
    # Mock the fetch_page method
    mock_html = """
    <html>
    <body>
        <a href="/documentation/swiftui/text">Text</a>
        <a href="/documentation/swiftui/button">Button</a>
        <a href="/documentation/swiftui/views">Views</a>
        <a href="/documentation/uikit/uilabel">UILabel</a>
        <a href="https://developer.apple.com/documentation/swiftui/image">Image</a>
    </body>
    </html>
    """
    
    with patch.object(scraper, 'fetch_page', new_callable=AsyncMock) as mock_fetch:
        mock_fetch.return_value = mock_html
        
        urls = await scraper.discover_urls()
        
        # Should discover SwiftUI URLs but not UIKit
        assert len(urls) >= 3
        assert any("text" in url for url in urls)
        assert any("button" in url for url in urls)
        assert not any("uikit" in url for url in urls)


@pytest.mark.asyncio
async def test_extract_availability():
    """Test extracting availability information."""
    scraper = AppleDocumentationScraper("swiftui")
    
    html = """
    <section class="availability">
        <span class="badge">iOS 13.0+</span>
        <span class="badge">macOS 10.15+</span>
        <span class="badge">tvOS 13.0+</span>
        <span class="badge">watchOS 6.0+</span>
    </section>
    """
    
    soup = BeautifulSoup(html, 'html.parser')
    availability = scraper._extract_availability(soup)
    
    assert len(availability) == 4
    assert availability[0]['platform'] == 'iOS'
    assert availability[0]['version'] == '13.0+'
    assert availability[1]['platform'] == 'macOS'
    assert availability[1]['version'] == '10.15+'


@pytest.mark.asyncio
async def test_extract_declaration():
    """Test extracting code declarations."""
    scraper = AppleDocumentationScraper("swiftui")
    
    html = """
    <section class="declaration">
        <pre><code class="language-swift">
@MainActor
struct Text : View {
    init(_ content: String)
}
        </code></pre>
        <pre><code class="language-objc">
@interface UILabel : UIView
@property(nonatomic, copy) NSString *text;
@end
        </code></pre>
    </section>
    """
    
    soup = BeautifulSoup(html, 'html.parser')
    declarations = scraper._extract_declaration(soup)
    
    assert 'swift' in declarations
    assert '@MainActor' in declarations['swift']
    assert 'struct Text : View' in declarations['swift']
    
    assert 'objc' in declarations
    assert '@interface UILabel' in declarations['objc']


@pytest.mark.asyncio
async def test_extract_code_examples():
    """Test extracting code examples."""
    scraper = AppleDocumentationScraper("swiftui")
    
    html = """
    <section class="code-example">
        <h3>Basic Text View</h3>
        <p>Create a simple text view:</p>
        <pre><code class="language-swift">
Text("Hello, World!")
    .font(.title)
    .foregroundColor(.blue)
        </code></pre>
    </section>
    """
    
    soup = BeautifulSoup(html, 'html.parser')
    examples = scraper._extract_code_examples(soup)
    
    assert len(examples) == 1
    assert examples[0]['title'] == 'Basic Text View'
    assert examples[0]['description'] == 'Create a simple text view:'
    assert 'Text("Hello, World!")' in examples[0]['code']
    assert examples[0]['language'] == 'swift'