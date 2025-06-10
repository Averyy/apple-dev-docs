# didReplaceTab(_:with:)

**Framework**: WebKit  
**Kind**: method

Should be called by the app when a tab is replaced by another tab to fire appropriate events with all loaded web extensions.

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

This method informs all loaded extensions of the replacement of a tab, ensuring consistent understanding across extensions.

If the intention is to inform only a specific extension, you should use the respective method on that extension’s context instead.

## Parameters

- `oldTab`: The tab that was replaced.
- `newTab`: The tab that replaced the old tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/didreplacetab(_:with:))*