# didOpenWindow(_:)

**Framework**: WebKit  
**Kind**: method

Should be called by the app when a new window is opened to fire appropriate events with all loaded web extensions.

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

This method informs all loaded extensions of the opening of a new window, ensuring consistent understanding across extensions.

If the intention is to inform only a specific extension, you should use the respective method on that extension’s context instead.

## Parameters

- `newWindow`: The newly opened window.

## See Also

- [func didCloseWindow(any WKWebExtensionWindow)](wkwebextensioncontroller/didclosewindow(_:).md)
  Should be called by the app when a window is closed to fire appropriate events with all loaded web extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/didopenwindow(_:))*