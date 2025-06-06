# parentTab(for:)

**Framework**: Webkit  
**Kind**: method

Called when the parent tab for the tab is needed.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func parentTab(for context: WKWebExtensionContext) -> (any WKWebExtensionTab)?
```

#### Discussion

Defaults to `nil` if not implemented.

## Parameters

- `context`: The context in which the web extension is running.

## See Also

- [func setParentTab((any WKWebExtensionTab)?, for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](wkwebextensiontab/setparenttab(_:for:completionhandler:).md)
  Called to set or clear the parent tab for the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/parenttab(for:))*