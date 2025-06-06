# didSelectTabs(_:)

**Framework**: Webkit  
**Kind**: method

Called by the app when tabs are selected to fire appropriate events with only this extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func didSelectTabs(_ selectedTabs: [any WKWebExtensionTab])
```

#### Discussion

This method informs only the specific extension that tabs have been selected. If the intention is to inform all loaded extensions consistently, you should use the respective method on the extension controller instead.

## Parameters

- `selectedTabs`: The set of tabs that were selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/didselecttabs(_:))*