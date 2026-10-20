# webView

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The view object that manages the web frame.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var webView: WebView! { get }
```

```objc
@property (nonatomic, strong, readonly) WebView * webView;
```

## See Also

### Getting Related Frames and Views
- [var parent: WebFrame!](./parent.md)
  The web frame’s parent web frame.
- [var childFrames: [Any]!](./childframes.md)
  The frames of the web frame’s immediate children.
- [var frameView: WebFrameView!](./frameview.md)
  The web frame’s view object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframe/webview)*