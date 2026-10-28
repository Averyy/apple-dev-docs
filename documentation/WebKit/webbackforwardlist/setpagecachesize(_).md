# setPageCacheSize(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Sets the maximum number of pages the receiver can cache.

**Availability**:
- macOS

> **Deprecated**: Use the [`usesPageCache`](../webpreferences/usespagecache.md) method in [`WebPreferences`](../webpreferences.md) instead.

## Declaration

```swift
func setPageCacheSize(_ size: Int)
```

```objc
- (void) setPageCacheSize:(NSUInteger) size;
```

## Discussion

The default page cache size can vary depending on the computer’s configuration. Use [`pageCacheSize()`](./pagecachesize%28%29.md) to get the current setting.

## Parameters

- `size`: The maximum number of pages that can be cached.

## See Also

### Page Caching
- [func pageCacheSize() -> Int](./pagecachesize%28%29.md)
  Returns the maximum number of pages that the receiver can cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webbackforwardlist/setpagecachesize(_:))*