# webView

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The web view that sent the message.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
weak var webView: WKWebView? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) WKWebView * webView;
```

## See Also

### Getting Message-Related Information
- [var frameInfo: WKFrameInfo](./frameinfo.md)
  The frame that sent the message.
- [var world: WKContentWorld](./world.md)
  The namespace in which the JavaScript code executes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkscriptmessage/webview)*