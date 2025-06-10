# didActivateTab(_:previousActiveTab:)

**Framework**: WebKit  
**Kind**: method

Called by the app when a tab is activated to notify only this specific extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@preconcurrency func didActivateTab(_ activatedTab: any WKWebExtensionTab, previousActiveTab previousTab: (any WKWebExtensionTab)? = nil)
```

#### Discussion

This method informs only the specific extension of the tab activation. If the intention is to inform all loaded extensions consistently, you should use the respective method on the extension controller instead.

## Parameters

- `activatedTab`: The tab that has become active.
- `previousTab`: The tab that was active before. This parameter can be   if there was no previously active tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/didactivatetab(_:previousactivetab:))*