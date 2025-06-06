# childFrames

**Framework**: Webkit  
**Kind**: property

The frames of the web frame’s immediate children.

**Availability**:
- macOS 10.3+

## Declaration

```swift
var childFrames: [Any]! { get }
```

#### Discussion

Each child web frame is an instance of `WebFrame` and corresponds to an HTML frameset or `iframe` element.

## See Also

- [var parent: WebFrame!](webframe/parent.md)
  The web frame’s parent web frame.
- [var frameView: WebFrameView!](webframe/frameview.md)
  The web frame’s view object.
- [var webView: WebView!](webframe/webview.md)
  The view object that manages the web frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframe/childframes)*