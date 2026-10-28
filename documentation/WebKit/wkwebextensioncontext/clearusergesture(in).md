# clearUserGesture(in:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called by the app to clear a user gesture in a specific tab.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
func clearUserGesture(in tab: any WKWebExtensionTab)
```

```objc
- (void) clearUserGestureInTab:(id<WKWebExtensionTab>) tab;
```

## Discussion

When a user gesture is no longer relevant in a tab, this method should be called to update the extension context.

This will revoke the extension’s access to features that require active user interaction, such as `activeTab`. User gestures are automatically cleared during navigation in certain scenarios; this method is needed if the app intends to clear the gesture more aggressively.

## Parameters

- `tab`: The tab from which the user gesture should be cleared.

## See Also

### Related Documentation
- [func userGesturePerformed(in: any WKWebExtensionTab)](./usergestureperformed%28in%29.md)
  Should be called by the app when a user gesture is performed in a specific tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/clearusergesture(in:))*