# isMuted(for:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called to check if the tab is currently muted.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
optional func isMuted(for context: WKWebExtensionContext) -> Bool
```

```objc
- (BOOL) isMutedForWebExtensionContext:(WKWebExtensionContext *) context;
```

#### Discussion

Defaults to `NO` if not implemented.

## Parameters

- `context`: The context in which the web extension is running.

## See Also

### Related Documentation
- [func setMuted(Bool, for: WKWebExtensionContext, completionHandler: ((any Error)?) -> Void)](./setmuted%28_,for,completionhandler%29.md)
  Called to set the mute state of the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/ismuted(for:))*