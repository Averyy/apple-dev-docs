# clearUserGesture(in:)

**Framework**: WebKit  
**Kind**: method

Called by the app to clear a user gesture in a specific tab.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func clearUserGesture(in tab: any WKWebExtensionTab)
```

#### Discussion

When a user gesture is no longer relevant in a tab, this method should be called to update the extension context.

This will revoke the extension’s access to features that require active user interaction, such as `activeTab`. User gestures are automatically cleared during navigation in certain scenarios; this method is needed if the app intends to clear the gesture more aggressively.

## Parameters

- `tab`: The tab from which the user gesture should be cleared.

## See Also

- [func userGesturePerformed(in: any WKWebExtensionTab)](wkwebextensioncontext/usergestureperformed(in:).md)
  Should be called by the app when a user gesture is performed in a specific tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/clearusergesture(in:))*