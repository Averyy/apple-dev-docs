# didMoveTab:fromIndex:inWindow:

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called by the app when a tab is moved to fire appropriate events with only this extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```objc
- (void) didMoveTab:(id<WKWebExtensionTab>) movedTab fromIndex:(NSUInteger) index inWindow:(id<WKWebExtensionWindow>) oldWindow;
```

#### Discussion

If the window is staying the same, the current window should be specified. This method informs only the specific extension that a tab has been moved. If the intention is to inform all loaded extensions consistently, you should use the respective method on the extension controller instead.

## Parameters

- `movedTab`: The tab that was moved.
- `index`: The old index of the tab within the window.
- `oldWindow`: The window that the tab was moved from, or `nil` if the tab isn’t moving from an open window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/didmovetab:fromindex:inwindow:)*