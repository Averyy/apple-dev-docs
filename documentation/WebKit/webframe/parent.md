# parent

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The web frame’s parent web frame.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var parent: WebFrame! { get }
```

```objc
@property (nonatomic, strong, readonly) WebFrame * parentFrame;
```

## See Also

### Getting Related Frames and Views
- [var childFrames: [Any]!](./childframes.md)
  The frames of the web frame’s immediate children.
- [var frameView: WebFrameView!](./frameview.md)
  The web frame’s view object.
- [var webView: WebView!](./webview.md)
  The view object that manages the web frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframe/parent)*