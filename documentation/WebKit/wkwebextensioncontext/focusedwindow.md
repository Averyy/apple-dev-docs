# focusedWindow

**Framework**: WebKit  
**Kind**: property

The window that currently has focus for this extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
weak var focusedWindow: (any WKWebExtensionWindow)? { get }
```

#### Discussion

Provides the window that currently has focus, as set by the [`didFocusWindow(_:)`](wkwebextensioncontext/didfocuswindow(_:).md) method.

It will be `nil` if no window has focus or if a window has focus that is not visible to the extension. Initially populated by the window returned by the extension controller delegate method [`webExtensionController(_:focusedWindowFor:)`](wkwebextensioncontrollerdelegate/webextensioncontroller(_:focusedwindowfor:).md).

## See Also

- [func didFocusWindow((any WKWebExtensionWindow)?)](wkwebextensioncontext/didfocuswindow(_:).md)
  Called by the app when a window gains focus to fire appropriate events with only this extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/focusedwindow)*