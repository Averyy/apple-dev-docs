# close()

**Framework**: WebKit  
**Kind**: method

Closes the web view when it’s no longer needed.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func close()
```

#### Discussion

Closes the web view by unloading its webpage and canceling any pending load requests. A closed web view no longer responds to new requests nor sends delegate messages. It is invoked automatically if the receiver’s enclosing window or host window is closed and sending [`shouldCloseWithWindow`](webview-swift.class/shouldclosewithwindow.md) to the receiver returns [`true`](https://developer.apple.com/documentation/swift/true). Use this method to stop the receiver from loading and sending delegate messages.

## See Also

- [var shouldCloseWithWindow: Bool](webview-swift.class/shouldclosewithwindow.md)
  A Boolean that indicates whether the web view should close when its window or host window closes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/close())*