# didActivateTab(_:previousActiveTab:)

**Framework**: Webkit  
**Kind**: method

Should be called by the app when a tab is activated to notify all loaded web extensions.

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

This method informs all loaded extensions of the tab activation, ensuring consistent state awareness across extensions.

If the intention is to inform only a specific extension, use the respective method on that extension’s context instead.

## Parameters

- `activatedTab`: The tab that has become active.
- `previousTab`: The tab that was active before. This parameter can be \c nil if there was no previously active tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/didactivatetab(_:previousactivetab:))*