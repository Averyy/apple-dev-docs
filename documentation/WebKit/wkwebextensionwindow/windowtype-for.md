# windowType(for:)

**Framework**: Webkit  
**Kind**: method

Called when the type of the window is needed.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func windowType(for context: WKWebExtensionContext) -> WKWebExtension.WindowType
```

#### Discussion

Defaults to[`WKWebExtension.WindowType.normal`](wkwebextension/windowtype/normal.md) if not implemented.

## Parameters

- `context`: The context in which the web extension is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensionwindow/windowtype(for:))*