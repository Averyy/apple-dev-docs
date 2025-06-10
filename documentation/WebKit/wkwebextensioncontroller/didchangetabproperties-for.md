# didChangeTabProperties(_:for:)

**Framework**: WebKit  
**Kind**: method

Should be called by the app when the properties of a tab are changed to fire appropriate events with all loaded web extensions.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func didChangeTabProperties(_ properties: WKWebExtension.TabChangedProperties, for changedTab: any WKWebExtensionTab)
```

#### Discussion

This method informs all loaded extensions of changes to tab properties, ensuring a unified understanding across extensions.

If the intention is to inform only a specific extension, you should use the respective method on that extension’s context instead.

## Parameters

- `properties`: The properties of the tab that were changed.
- `changedTab`: The tab whose properties were changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/didchangetabproperties(_:for:))*