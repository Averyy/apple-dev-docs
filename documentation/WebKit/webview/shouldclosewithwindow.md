# shouldCloseWithWindow

**Framework**: Webkit  
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

If [`true`](https://developer.apple.com/documentation/swift/true), the web view should close; otherwise, it should not.

## See Also

- [func close()](webview/close.md)
  Closes the web view when it’s no longer needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/shouldclosewithwindow)*