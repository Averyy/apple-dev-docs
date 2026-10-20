# usesPageCache

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the web views associated with the receiver should use the shared page cache.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var usesPageCache: Bool { get set }
```

```objc
@property (nonatomic) BOOL usesPageCache;
```

#### Discussion

[`true`](../../Swift/true.md) if the web views should use a page cache; otherwise, [`false`](../../Swift/false.md).

Pages are cached when they are added to a back-forward list, and removed from the cache when they are removed from a back-forward list. Because the page cache is global, caching a page in one back-forward list may cause a page in another back-forward list to be removed from the cache.

## See Also

### Caching
- [var cacheModel: WebCacheModel](./cachemodel.md)
  The cache model for the web views associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpreferences/usespagecache)*