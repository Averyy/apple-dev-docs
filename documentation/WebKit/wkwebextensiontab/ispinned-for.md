# isPinned(for:)

**Framework**: Webkit  
**Kind**: method

Called when the pinned state of the tab is needed.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func isPinned(for context: WKWebExtensionContext) -> Bool
```

#### Discussion

Defaults to `NO` if not implemented.

## Parameters

- `context`: The context in which the web extension is running.

## See Also

- [func setPinned(Bool, for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](wkwebextensiontab/setpinned(_:for:completionhandler:).md)
  Called to set the pinned state of the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/ispinned(for:))*