# WebCacheModel

**Framework**: WebKit  
**Kind**: enum  
**Role**: Enumeration

Specifies the caching model for a web view.

**Availability**:
- macOS 10.5+ - Deprecated in 10.14

## Declaration

```swift
enum WebCacheModel
```

```c
enum WebCacheModel : NSUInteger;
```

## Topics

### Constants
- [WebCacheModel.documentViewer](./webcachemodel/documentviewer.md)
  Releases resources when they are no longer referenced and caches remote resources on disk. This model is appropriate for displaying a static document with no navigation user interface. This is the most memory-efficient model.
- [WebCacheModel.documentBrowser](./webcachemodel/documentbrowser.md)
  Caches a reasonable number of resources and previously viewed documents in memory and on disk. This model is appropriate for displaying and navigating between multiple documents.
- [WebCacheModel.primaryWebBrowser](./webcachemodel/primarywebbrowser.md)
  Caches a large number of resources and previously viewed documents in memory and on disk. This model is appropriate for a web view that behaves like a web browser.
### Initializers
- [init?(rawValue: UInt)](./webcachemodel/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webcachemodel)*