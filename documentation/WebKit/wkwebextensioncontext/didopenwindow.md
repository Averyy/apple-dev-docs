# didOpenWindow(_:)

**Framework**: WebKit  
**Kind**: method

Called by the app when a new window is opened to fire appropriate events with only this extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func didOpenWindow(_ newWindow: any WKWebExtensionWindow)
```

#### Discussion

This method informs only the specific extension of the opening of a new window. If the intention is to inform all loaded extensions consistently, you should use the respective method on the extension controller instead.

## Parameters

- `newWindow`: The newly opened window.

## See Also

- [func didCloseWindow(any WKWebExtensionWindow)](wkwebextensioncontext/didclosewindow(_:).md)
  Called by the app when a window is closed to fire appropriate events with only this extension.
- [var openWindows: [any WKWebExtensionWindow]](wkwebextensioncontext/openwindows.md)
  The open windows that are exposed to this extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/didopenwindow(_:))*