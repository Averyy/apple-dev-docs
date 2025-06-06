# didMoveTab(_:from:in:)

**Framework**: Webkit  
**Kind**: method

Should be called by the app when a tab is moved to fire appropriate events with all loaded web extensions.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@preconcurrency func didMoveTab(_ movedTab: any WKWebExtensionTab, from index: Int, in oldWindow: (any WKWebExtensionWindow)? = nil)
```

#### Discussion

This method informs all loaded extensions of the movement of a tab, ensuring consistent understanding across extensions.

If the window is staying the same, the current window should be specified. If the intention is to inform only a specific extension, use the respective method on that extension’s context instead.

## Parameters

- `movedTab`: The tab that was moved.
- `index`: The old index of the tab within the window.
- `oldWindow`: The window that the tab was moved from, or   if the tab is moving from no open window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/didmovetab(_:from:in:))*