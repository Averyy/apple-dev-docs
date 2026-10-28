# childFrames

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The frames of the web frame’s immediate children.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var childFrames: [Any]! { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray * childFrames;
```

## Discussion

Each child web frame is an instance of `WebFrame` and corresponds to an HTML frameset or `iframe` element.

## See Also

### Getting Related Frames and Views
- [var parent: WebFrame!](./parent.md)
  The web frame’s parent web frame.
- [var frameView: WebFrameView!](./frameview.md)
  The web frame’s view object.
- [var webView: WebView!](./webview.md)
  The view object that manages the web frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframe/childframes)*