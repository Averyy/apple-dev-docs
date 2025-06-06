# isMuted(for:)

**Framework**: Webkit  
**Kind**: method

Called to check if the tab is currently muted.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func isMuted(for context: WKWebExtensionContext) -> Bool
```

#### Discussion

Defaults to `NO` if not implemented.

## Parameters

- `context`: The context in which the web extension is running.

## See Also

- [func setMuted(Bool, for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](wkwebextensiontab/setmuted(_:for:completionhandler:).md)
  Called to set the mute state of the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/ismuted(for:))*