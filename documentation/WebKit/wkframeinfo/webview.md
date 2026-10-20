# webView

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The web view that contains this frame and the containing webpage.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
weak var webView: WKWebView? { get }
```

```objc
@property (nonatomic, weak, readonly) WKWebView * webView;
```

## See Also

### Inspecting frame information
- [var isMainFrame: Bool](./ismainframe.md)
  A Boolean value indicating whether the frame is the web site’s main frame or a subframe.
- [var request: URLRequest](./request.md)
  The frame’s current request.
- [var securityOrigin: WKSecurityOrigin](./securityorigin.md)
  The frame’s security origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkframeinfo/webview)*