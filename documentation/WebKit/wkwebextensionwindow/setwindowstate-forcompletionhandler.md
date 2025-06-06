# setWindowState(_:for:completionHandler:)

**Framework**: Webkit  
**Kind**: method

Called to set the state of the window.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func setWindowState(_ state: WKWebExtension.WindowState, for context: WKWebExtensionContext) async throws
```

#### Discussion

The implementation of [`windowState(for:)`](wkwebextensionwindow/windowstate(for:).md) is a prerequisite.

Without it, this method will not be called.

## Parameters

- `state`: The new state of the window.
- `context`: The context in which the web extension is running.
- `completionHandler`: A block that must be called upon completion. It takes a single error argument, which should be provided if any errors occurred.

## See Also

- [func windowState(for: WKWebExtensionContext) -> WKWebExtension.WindowState](wkwebextensionwindow/windowstate(for:).md)
  Called when the state of the window is needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensionwindow/setwindowstate(_:for:completionhandler:))*