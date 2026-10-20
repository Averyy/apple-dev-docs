# pageCacheSize()

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns the maximum number of pages that the receiver can cache.

**Availability**:
- macOS

> **Deprecated**: Use the [`usesPageCache`](../webpreferences/usespagecache.md) method in [`WebPreferences`](../webpreferences.md) instead.

## Declaration

```swift
func pageCacheSize() -> Int
```

```objc
- (NSUInteger) pageCacheSize;
```

#### Return Value

The maximum number of pages that can be cached.

## See Also

### Page Caching
- [func setPageCacheSize(Int)](./setpagecachesize%28_%29.md)
  Sets the maximum number of pages the receiver can cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webbackforwardlist/pagecachesize())*