# userGesturePerformed(in:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Should be called by the app when a user gesture is performed in a specific tab.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
func userGesturePerformed(in tab: any WKWebExtensionTab)
```

```objc
- (void) userGesturePerformedInTab:(id<WKWebExtensionTab>) tab;
```

#### Discussion

When a user gesture is performed in a tab, this method should be called to update the extension context.

This enables the extension to be aware of the user gesture, potentially granting it access to features that require user interaction, such as `activeTab`. Not required if using [`performAction(for:)`](./performaction%28for%29.md).

## Parameters

- `tab`: The tab in which the user gesture was performed.

## See Also

### Related Documentation
- [func hasActiveUserGesture(in: any WKWebExtensionTab) -> Bool](./hasactiveusergesture%28in%29.md)
  Indicates if a user gesture is currently active in the specified tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/usergestureperformed(in:))*