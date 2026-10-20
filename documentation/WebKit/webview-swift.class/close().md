# close()

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Closes the web view when it’s no longer needed.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
func close()
```

```objc
- (void) close;
```

#### Discussion

Closes the web view by unloading its webpage and canceling any pending load requests. A closed web view no longer responds to new requests nor sends delegate messages. It is invoked automatically if the receiver’s enclosing window or host window is closed and sending [`shouldCloseWithWindow`](./shouldclosewithwindow.md) to the receiver returns [`true`](../../Swift/true.md). Use this method to stop the receiver from loading and sending delegate messages.

## See Also

### Closing the View
- [var shouldCloseWithWindow: Bool](./shouldclosewithwindow.md)
  A Boolean that indicates whether the web view should close when its window or host window closes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/close())*