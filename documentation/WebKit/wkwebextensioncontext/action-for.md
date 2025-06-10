# action(for:)

**Framework**: WebKit  
**Kind**: method

Retrieves the extension action for a given tab, or the default action if `nil` is passed.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func action(for tab: (any WKWebExtensionTab)?) -> WKWebExtension.Action?
```

#### Discussion

The returned object represents the action specific to the tab when provided; otherwise, it returns the default action. The default action is useful when the context is unrelated to a specific tab. When possible, specify the tab to get the most context-relevant action.

## Parameters

- `tab`: The tab for which to retrieve the extension action, or   to get the default action.

## See Also

- [func performAction(for: (any WKWebExtensionTab)?)](wkwebextensioncontext/performaction(for:).md)
  Performs the extension action associated with the specified tab or performs the default action if `nil` is passed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/action(for:))*