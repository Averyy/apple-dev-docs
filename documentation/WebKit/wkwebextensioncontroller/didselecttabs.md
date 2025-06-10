# didSelectTabs(_:)

**Framework**: WebKit  
**Kind**: method

Should be called by the app when tabs are selected to fire appropriate events with all loaded web extensions.

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

This method informs all loaded extensions that tabs have been selected, ensuring consistent understanding across extensions.

If the intention is to inform only a specific extension, you should use the respective method on that extension’s context instead.

## Parameters

- `selectedTabs`: The set of tabs that were selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/didselecttabs(_:))*