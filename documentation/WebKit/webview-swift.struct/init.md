# init(_:)

**Framework**: WebKit  
**Kind**: init

Create a new WebView.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@preconcurrency init(_ page: WebPage)
```

## Parameters

- `page`: The   that should be associated with this  . It is a programming error to create multiple  s with the same  .

## See Also

- [init(url: URL?)](webview-swift.struct/init(url:).md)
  Create a new WebView with the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.struct/init(_:))*