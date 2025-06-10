# request

**Framework**: WebKit  
**Kind**: property

The frame’s current request.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var request: URLRequest { get }
```

## See Also

- [var isMainFrame: Bool](wkframeinfo/ismainframe.md)
  A Boolean value indicating whether the frame is the web site’s main frame or a subframe.
- [var securityOrigin: WKSecurityOrigin](wkframeinfo/securityorigin.md)
  The frame’s security origin.
- [var webView: WKWebView?](wkframeinfo/webview.md)
  The web view that contains this frame and the containing webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkframeinfo/request)*