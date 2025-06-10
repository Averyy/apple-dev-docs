# isSelected(for:)

**Framework**: WebKit  
**Kind**: method

Called when the selected state of the tab is needed.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func isSelected(for context: WKWebExtensionContext) -> Bool
```

#### Discussion

Defaults to `YES` for the active tab and `NO` for other tabs if not implemented.

## Parameters

- `context`: The context in which the web extension is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/isselected(for:))*