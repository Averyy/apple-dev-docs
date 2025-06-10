# windowState(for:)

**Framework**: WebKit  
**Kind**: method

Called when the state of the window is needed.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func windowState(for context: WKWebExtensionContext) -> WKWebExtension.WindowState
```

#### Discussion

Defaults to[`WKWebExtension.WindowState.normal`](wkwebextension/windowstate/normal.md) if not implemented.

## Parameters

- `context`: The context in which the web extension is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensionwindow/windowstate(for:))*