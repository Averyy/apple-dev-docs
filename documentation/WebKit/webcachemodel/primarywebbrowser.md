# WebCacheModel.primaryWebBrowser

**Framework**: Webkit  
**Kind**: case

Caches a large number of resources and previously viewed documents in memory and on disk. This model is appropriate for a web view that behaves like a web browser.

**Availability**:
- macOS 10.5+

## Declaration

```swift
case primaryWebBrowser
```

## See Also

- [WebCacheModel.documentViewer](webcachemodel/documentviewer.md)
  Releases resources when they are no longer referenced and caches remote resources on disk. This model is appropriate for displaying a static document with no navigation user interface. This is the most memory-efficient model.
- [WebCacheModel.documentBrowser](webcachemodel/documentbrowser.md)
  Caches a reasonable number of resources and previously viewed documents in memory and on disk. This model is appropriate for displaying and navigating between multiple documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webcachemodel/primarywebbrowser)*