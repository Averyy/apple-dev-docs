# frame(for:)

**Framework**: Webkit  
**Kind**: method

Called when the frame of the window is needed.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func frame(for context: WKWebExtensionContext) -> CGRect
```

#### Discussion

Defaults to [`CGRectNull`](https://developer.apple.com/documentation/CoreGraphics/CGRectNull) if not implemented.

## Parameters

- `context`: The context in which the web extension is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensionwindow/frame(for:))*