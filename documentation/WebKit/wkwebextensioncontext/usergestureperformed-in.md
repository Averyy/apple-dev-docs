# userGesturePerformed(in:)

**Framework**: WebKit  
**Kind**: method

Should be called by the app when a user gesture is performed in a specific tab.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func userGesturePerformed(in tab: any WKWebExtensionTab)
```

#### Discussion

When a user gesture is performed in a tab, this method should be called to update the extension context.

This enables the extension to be aware of the user gesture, potentially granting it access to features that require user interaction, such as `activeTab`. Not required if using [`performAction(for:)`](wkwebextensioncontext/performaction(for:).md).

## Parameters

- `tab`: The tab in which the user gesture was performed.

## See Also

- [func hasActiveUserGesture(in: any WKWebExtensionTab) -> Bool](wkwebextensioncontext/hasactiveusergesture(in:).md)
  Indicates if a user gesture is currently active in the specified tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/usergestureperformed(in:))*