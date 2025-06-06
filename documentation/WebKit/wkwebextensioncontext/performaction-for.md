# performAction(for:)

**Framework**: Webkit  
**Kind**: method

Performs the extension action associated with the specified tab or performs the default action if `nil` is passed.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func performAction(for tab: (any WKWebExtensionTab)?)
```

#### Discussion

Performing the action will mark the tab, if specified, as having an active user gesture. When the `tab` parameter is `nil`, the default action is performed. The action can either trigger an event or display a popup, depending on how the extension is configured.

If the action is configured to display a popup, implementing the appropriate web extension controller delegate method is required; otherwise, no action is performed for popup actions.

## Parameters

- `tab`: The tab for which to perform the extension action, or   to perform the default action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/performaction(for:))*