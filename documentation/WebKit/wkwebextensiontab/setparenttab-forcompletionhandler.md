# setParentTab(_:for:completionHandler:)

**Framework**: WebKit  
**Kind**: method

Called to set or clear the parent tab for the tab.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func setParentTab(_ parentTab: (any WKWebExtensionTab)?, for context: WKWebExtensionContext) async throws
```

#### Discussion

No action is performed if not implemented.

## Parameters

- `parentTab`: The tab that should be set as the parent of the tab. If \c nil is provided, the current parent tab should be cleared.
- `context`: The context in which the web extension is running.
- `completionHandler`: A block that must be called upon completion. It takes a single error argument, which should be provided if any errors occurred.

## See Also

- [func parentTab(for: WKWebExtensionContext) -> (any WKWebExtensionTab)?](wkwebextensiontab/parenttab(for:).md)
  Called when the parent tab for the tab is needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/setparenttab(_:for:completionhandler:))*