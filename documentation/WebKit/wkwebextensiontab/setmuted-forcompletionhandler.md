# setMuted(_:for:completionHandler:)

**Framework**: Webkit  
**Kind**: method

Called to set the mute state of the tab.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func setMuted(_ muted: Bool, for context: WKWebExtensionContext) async throws
```

#### Discussion

No action is performed if not implemented.

## Parameters

- `muted`: A boolean indicating whether the tab should be muted.
- `context`: The context in which the web extension is running.
- `completionHandler`: A block that must be called upon completion. It takes a single error argument, which should be provided if any errors occurred.

## See Also

- [func isMuted(for: WKWebExtensionContext) -> Bool](wkwebextensiontab/ismuted(for:).md)
  Called to check if the tab is currently muted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/setmuted(_:for:completionhandler:))*