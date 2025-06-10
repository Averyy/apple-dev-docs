# setPageCacheSize(_:)

**Framework**: WebKit  
**Kind**: method

Sets the maximum number of pages the receiver can cache.

**Availability**:
- macOS ?+

## Declaration

```swift
func setPageCacheSize(_ size: Int)
```

#### Discussion

The default page cache size can vary depending on the computer’s configuration. Use [`pageCacheSize()`](webbackforwardlist/pagecachesize().md) to get the current setting.

## Parameters

- `size`: The maximum number of pages that can be cached.

## See Also

- [func pageCacheSize() -> Int](webbackforwardlist/pagecachesize.md)
  Returns the maximum number of pages that the receiver can cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webbackforwardlist/setpagecachesize(_:))*