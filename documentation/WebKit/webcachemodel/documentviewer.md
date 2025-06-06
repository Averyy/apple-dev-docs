# WebCacheModel.documentViewer

**Framework**: Webkit  
**Kind**: case

Releases resources when they are no longer referenced and caches remote resources on disk. This model is appropriate for displaying a static document with no navigation user interface. This is the most memory-efficient model.

**Availability**:
- macOS 10.5+

## Declaration

```swift
case documentViewer
```

## See Also

- [WebCacheModel.documentBrowser](webcachemodel/documentbrowser.md)
  Caches a reasonable number of resources and previously viewed documents in memory and on disk. This model is appropriate for displaying and navigating between multiple documents.
- [WebCacheModel.primaryWebBrowser](webcachemodel/primarywebbrowser.md)
  Caches a large number of resources and previously viewed documents in memory and on disk. This model is appropriate for a web view that behaves like a web browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webcachemodel/documentviewer)*