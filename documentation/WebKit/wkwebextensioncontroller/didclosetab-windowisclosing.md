# didCloseTab(_:windowIsClosing:)

**Framework**: WebKit  
**Kind**: method

Should be called by the app when a tab is closed to fire appropriate events with all loaded web extensions.

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

This method informs all loaded extensions of the closing of a tab, ensuring consistent understanding across extensions.

If the intention is to inform only a specific extension, you should use the respective method on that extension’s context instead.

## Parameters

- `closedTab`: The tab that was closed.
- `windowIsClosing`: A boolean value indicating whether the window containing the tab is also closing.

## See Also

- [func didOpenTab(any WKWebExtensionTab)](wkwebextensioncontroller/didopentab(_:).md)
  Should be called by the app when a new tab is opened to fire appropriate events with all loaded web extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/didclosetab(_:windowisclosing:))*