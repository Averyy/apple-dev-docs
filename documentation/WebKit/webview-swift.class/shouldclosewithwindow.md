# shouldCloseWithWindow

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the web view should close when its window or host window closes.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
var shouldCloseWithWindow: Bool { get set }
```

```objc
@property (nonatomic) BOOL shouldCloseWithWindow;
```

## Discussion

If [`true`](../../Swift/true.md), the web view should close; otherwise, it should not.

## See Also

### Closing the View
- [func close()](./close%28%29.md)
  Closes the web view when it’s no longer needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/shouldclosewithwindow)*