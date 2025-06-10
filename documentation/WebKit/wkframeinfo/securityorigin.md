# securityOrigin

**Framework**: WebKit  
**Kind**: property

The frame’s security origin.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var securityOrigin: WKSecurityOrigin { get }
```

#### Discussion

The [`WKSecurityOrigin`](wksecurityorigin.md) object consists of a host name, a protocol, and a port number.

## See Also

- [var isMainFrame: Bool](wkframeinfo/ismainframe.md)
  A Boolean value indicating whether the frame is the web site’s main frame or a subframe.
- [var request: URLRequest](wkframeinfo/request.md)
  The frame’s current request.
- [var webView: WKWebView?](wkframeinfo/webview.md)
  The web view that contains this frame and the containing webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkframeinfo/securityorigin)*