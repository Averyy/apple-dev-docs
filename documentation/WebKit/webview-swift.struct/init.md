# init(_:)

**Framework**: WebKit  
**Kind**: init

Create a new WebView.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ page: WebPage)
```

## Parameters

- `page`: The [`WebPage`](webpage.md) that should be associated with this [`WebView`](webview-swift.struct.md). It is a programming error to create multiple [`WebView`](webview-swift.struct.md)s with the same [`WebPage`](webpage.md).

## See Also

- [init(url: URL?)](webview-swift.struct/init(url:).md)
  Create a new WebView with the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.struct/init(_:))*