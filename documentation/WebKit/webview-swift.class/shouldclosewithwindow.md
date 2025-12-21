# shouldCloseWithWindow

**Framework**: WebKit  
**Kind**: property

A Boolean that indicates whether the web view should close when its window or host window closes.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
var shouldCloseWithWindow: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), the web view should close; otherwise, it should not.

## See Also

- [func close()](webview-swift.class/close.md)
  Closes the web view when it’s no longer needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/shouldclosewithwindow)*