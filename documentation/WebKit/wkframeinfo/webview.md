# webView

**Framework**: Webkit  
**Kind**: property

The web view that contains this frame and the containing webpage.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var webView: WKWebView? { get }
```

## See Also

- [var isMainFrame: Bool](wkframeinfo/ismainframe.md)
  A Boolean value indicating whether the frame is the web site’s main frame or a subframe.
- [var request: URLRequest](wkframeinfo/request.md)
  The frame’s current request.
- [var securityOrigin: WKSecurityOrigin](wkframeinfo/securityorigin.md)
  The frame’s security origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkframeinfo/webview)*