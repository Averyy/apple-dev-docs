# didCloseWindow(_:)

**Framework**: WebKit  
**Kind**: method

Should be called by the app when a window is closed to fire appropriate events with all loaded web extensions.

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

- closedWindow: The window that was closed.

This method informs all loaded extensions of the closure of a window, ensuring consistent understanding across extensions.

If the intention is to inform only a specific extension, you should use the respective method on that extension’s context instead.

## See Also

- [func didOpenWindow(any WKWebExtensionWindow)](wkwebextensioncontroller/didopenwindow(_:).md)
  Should be called by the app when a new window is opened to fire appropriate events with all loaded web extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/didclosewindow(_:))*