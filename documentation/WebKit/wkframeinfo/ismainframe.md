# isMainFrame

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the frame is the web site’s main frame or a subframe.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
var isMainFrame: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isMainFrame) BOOL mainFrame;
```

## See Also

### Inspecting frame information
- [var request: URLRequest](./request.md)
  The frame’s current request.
- [var securityOrigin: WKSecurityOrigin](./securityorigin.md)
  The frame’s security origin.
- [var webView: WKWebView?](./webview.md)
  The web view that contains this frame and the containing webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkframeinfo/ismainframe)*