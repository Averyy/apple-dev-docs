# tabs(for:)

**Framework**: Webkit  
**Kind**: method

Called when the tabs are needed for the window.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func tabs(for context: WKWebExtensionContext) -> [any WKWebExtensionTab]
```

#### Discussion

Defaults to an empty array if not implemented.

## Parameters

- `context`: The context in which the web extension is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensionwindow/tabs(for:))*