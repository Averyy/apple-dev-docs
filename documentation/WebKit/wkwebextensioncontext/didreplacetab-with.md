# didReplaceTab(_:with:)

**Framework**: Webkit  
**Kind**: method

Called by the app when a tab is replaced by another tab to fire appropriate events with only this extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func didReplaceTab(_ oldTab: any WKWebExtensionTab, with newTab: any WKWebExtensionTab)
```

#### Discussion

This method informs only the specific extension that a tab has been replaced. If the intention is to inform all loaded extensions consistently, you should use the respective method on the extension controller instead.

## Parameters

- `oldTab`: The tab that was replaced.
- `newTab`: The tab that replaced the old tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/didreplacetab(_:with:))*