# cacheModel

**Framework**: Webkit  
**Kind**: property

The cache model for the web views associated with the receiver.

**Availability**:
- macOS 10.3+

## Declaration

```swift
var cacheModel: WebCacheModel { get set }
```

#### Discussion

Possible values are described in [`WebCacheModel`](webcachemodel.md).

Set this property to optimize WebKit’s cache footprint (on disk and in memory) to best fit the use of the web view. If a web view is used only for a single webpage, use the [`WebCacheModel.documentViewer`](webcachemodel/documentviewer.md) constant instead.

## See Also

- [var usesPageCache: Bool](webpreferences/usespagecache.md)
  A Boolean that indicates whether the web views associated with the receiver should use the shared page cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpreferences/cachemodel)*