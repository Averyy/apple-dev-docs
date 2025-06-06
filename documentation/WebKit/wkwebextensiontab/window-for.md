# window(for:)

**Framework**: Webkit  
**Kind**: method

Called when the window containing the tab is needed.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func window(for context: WKWebExtensionContext) -> (any WKWebExtensionWindow)?
```

#### Discussion

Defaults to `nil` if not implemented.

## Parameters

- `context`: The context in which the web extension is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/window(for:))*