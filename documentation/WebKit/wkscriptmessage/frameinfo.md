# frameInfo

**Framework**: WebKit  
**Kind**: property

The frame that sent the message.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var frameInfo: WKFrameInfo { get }
```

## See Also

- [var webView: WKWebView?](wkscriptmessage/webview.md)
  The web view that sent the message.
- [var world: WKContentWorld](wkscriptmessage/world.md)
  The namespace in which the JavaScript code executes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkscriptmessage/frameinfo)*