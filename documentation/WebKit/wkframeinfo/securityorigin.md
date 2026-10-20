# securityOrigin

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The frame’s security origin.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var securityOrigin: WKSecurityOrigin { get }
```

```objc
@property (nonatomic, readonly) WKSecurityOrigin * securityOrigin;
```

#### Discussion

The [`WKSecurityOrigin`](../wksecurityorigin.md) object consists of a host name, a protocol, and a port number.

## See Also

### Inspecting frame information
- [var isMainFrame: Bool](./ismainframe.md)
  A Boolean value indicating whether the frame is the web site’s main frame or a subframe.
- [var request: URLRequest](./request.md)
  The frame’s current request.
- [var webView: WKWebView?](./webview.md)
  The web view that contains this frame and the containing webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkframeinfo/securityorigin)*