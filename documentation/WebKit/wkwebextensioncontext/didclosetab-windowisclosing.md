# didCloseTab(_:windowIsClosing:)

**Framework**: WebKit  
**Kind**: method

Called by the app when a tab is closed to fire appropriate events with only this extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@preconcurrency func didCloseTab(_ closedTab: any WKWebExtensionTab, windowIsClosing: Bool = false)
```

#### Discussion

This method informs only the specific extension of the closure of a tab. If the intention is to inform all loaded extensions consistently, you should use the respective method on the extension controller instead.

## Parameters

- `closedTab`: The tab that was closed.
- `windowIsClosing`: A Boolean value indicating whether the window containing the tab is also closing.

## See Also

- [func didOpenTab(any WKWebExtensionTab)](wkwebextensioncontext/didopentab(_:).md)
  Called by the app when a new tab is opened to fire appropriate events with only this extension.
- [var openTabs: Set<AnyHashable>](wkwebextensioncontext/opentabs.md)
  A set of open tabs in all open windows that are exposed to this extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/didclosetab(_:windowisclosing:))*