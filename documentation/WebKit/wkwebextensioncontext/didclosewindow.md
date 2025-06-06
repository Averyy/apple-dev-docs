# didCloseWindow(_:)

**Framework**: Webkit  
**Kind**: method

Called by the app when a window is closed to fire appropriate events with only this extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func didCloseWindow(_ closedWindow: any WKWebExtensionWindow)
```

#### Discussion

This method informs only the specific extension of the closure of a window. If the intention is to inform all loaded extensions consistently, you should use the respective method on the extension controller instead.

## Parameters

- `closedWindow`: The window that was closed.

## See Also

- [func didOpenWindow(any WKWebExtensionWindow)](wkwebextensioncontext/didopenwindow(_:).md)
  Called by the app when a new window is opened to fire appropriate events with only this extension.
- [var openWindows: [any WKWebExtensionWindow]](wkwebextensioncontext/openwindows.md)
  The open windows that are exposed to this extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/didclosewindow(_:))*