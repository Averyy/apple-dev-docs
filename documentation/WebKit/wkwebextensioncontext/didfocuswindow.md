# didFocusWindow(_:)

**Framework**: WebKit  
**Kind**: method

Called by the app when a window gains focus to fire appropriate events with only this extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func didFocusWindow(_ focusedWindow: (any WKWebExtensionWindow)?)
```

#### Discussion

This method informs only the specific extension that a window has gained focus. If the intention is to inform all loaded extensions consistently, you should use the respective method on the extension controller instead.

## Parameters

- `focusedWindow`: The window that gained focus, or   if no window has focus or a window has focus that is not visible to this extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/didfocuswindow(_:))*